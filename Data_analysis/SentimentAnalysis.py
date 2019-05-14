import os
import json
from pprint import pprint
import pandas as pd
import couchdb
from reactionrnn import reactionrnn
import re
import numpy as np

#connect to couchdb server. A database will be returned
def connect_couchdb(add,dbname):

    address = add
    user = "admin"
    password = "nmsl"
    
    
    
    
    #connect to couchdb server
    
    couchserver = couchdb.Server(address)

    db = couchserver[dbname]
    
    return db

#sentiment value calculation
def angry_calculation(db):
    react = reactionrnn()

    city = []
    angry = []
    TwitterText =[]
    coordinates =[]
    for item in db.view('_design/text_extract/_view/new-view'):

        if item.value not in TwitterText:
            TwitterText.append(item.value)
            #remove URLs
            text_noURL = re.sub(r"http\S+", "", item.value)
            #remove username 
            text = re.sub(r"@\w+", "", text_noURL).lstrip()
            #if text.isspace() is False:
            #print(text)
            coordinates.append(item.key['bounding_box']['coordinates'])
            angry_value = react.predict(text)['angry']
            angry.append(angry_value)
            city.append(item.key['full_name'])

    d = {'angry':angry,'full_name':city,'coordinates':coordinates}
    df = pd.DataFrame(data = d)
    return df

# reuturn dataframe with city, angry value and number of tweets in each city
def angry_dataFrame(df):
    
    city_angry = df.groupby(['full_name']).sum()
    city_NumTweet = df.groupby(['full_name']).count()

    city_list = city_angry.index.tolist()
    Normalized_AngryValue = city_angry['angry']/city_NumTweet['coordinates']

    angryDF = {'angry_value': Normalized_AngryValue,'Number of Tweets': city_NumTweet['coordinates'],'full_name':city_list}
    dff = pd.DataFrame(data = angryDF).reset_index(drop = True)

    finalDF = dff.merge(df.drop_duplicates(subset = ['full_name'],keep = 'first'),
                        on = 'full_name', how = 'left').drop(columns = ['angry'])
    
    city = finalDF['full_name'].str.split(',',n=1,expand = True)
    sepCity = pd.DataFrame({'city':city.loc[:,0], 'state':city.loc[:,1]})

    sepCityDF = finalDF.join(sepCity).sort_values(['state', 'Number of Tweets'], 
                                                  ascending=[True, False]).groupby('state').head(10)
    
    return sepCityDF

#add punish term to angry value calculation if number of tweets in a city less than a specific value
def punisher_NumTweet(finalDF):
    for index,row in finalDF.iterrows():
    #    print(row['angry_value'])
        if row['Number of Tweets'] <= 100:
            row['angry_value'] = row['angry_value'] *(row['Number of Tweets']/(100-row['Number of Tweets']))
        finalDF.at[index,'angry_value'] = row['angry_value']
    return finalDF

def angValue_normalization(sepCityDF):
#    if sepCityDF['Number of Tweets']< 100:
        
    sepCityDF['angry_value'] = (sepCityDF['angry_value']-
                                sepCityDF['angry_value'].min())/(sepCityDF['angry_value'].max()-
                                                                 sepCityDF['angry_value'].min())*(100-1)+1
    return sepCityDF

def state_summary(sepCityDF):
    state_value = sepCityDF.groupby(['state']).sum()
    state_value['angry_value'] = state_value['angry_value']/state_value['Number of Tweets']
    #interpolation normalization
    state_value['angry_value'] = ((state_value['angry_value']-
                                  state_value['angry_value'].min())/(state_value['angry_value'].max()-
                                                                     state_value['angry_value'].min())) *(100-1)+1
    state_value['angry_value'] = (np.log(state_value['angry_value'])/np.log(10))*50
    return state_value

def sentiment_merge_aurin(sepCityDF,aurinDFF):
    sepCityDF = sepCityDF.reset_index().drop(columns = ['index'])
    sepCityDF_aurin = sepCityDF.merge(aurinDFF, on='city', how = 'left').drop(columns = ['full_name']).fillna(1)
    sepCityDF_aurin['unemploy_Rate'] = round(sepCityDF_aurin['unemploy_Rate'],2)
    sepCityDF_aurin['angry_value'] = round(sepCityDF_aurin['angry_value'],2)
    return sepCityDF_aurin

def generate_geojson_state_city(sepCityDF_aurin, ct):
    for index,row in sepCityDF_aurin.iterrows():

        for city in ct['features']:
            try:
                if city['properties']['city'] == row['city']:
                    city['properties']['angry_value'] = round(row['angry_value'],2)
                    city['properties']['median_income'] = int(row['median_aud'])
                    city['properties']['labor_force_median_age'] = int(row['median_age_of_earners_years'])
                    #print(city['properties']['angry_value'])
                    city['properties']['tweets_number'] = int(row['Number of Tweets'])
                    city['properties']['unemployment_rate'] = row['unemploy_Rate']
                    #print(city['properties']['tweets_number'])
            except KeyError:
    #            print('no such city')
                continue
    with open('forFrontEnd.json', 'w') as outfile:
        json.dump(ct, outfile)          
    
    return ct

def state_combine_aurin(state_sum,aurinData):

    state_sum.reset_index(level=0, inplace=True)
    state_sum['state'] = state_sum['state'].str.lstrip()

    stateData = pd.read_excel(aurinData)

    state_sum_aurin = stateData.merge(state_sum, left_on = 'state',right_on = 'state',how = 'outer', )
    state_sum_aurin['angry_value'] = round(state_sum_aurin['angry_value'],2)
    state_sum_aurin['unemploy_rate'] = round(state_sum_aurin['unemploy_rate'],2)
    return state_sum_aurin

def generate_geojson_state(state_sum_aurin,state):
    for index,row in state_sum_aurin.iterrows():

        for st in state['features']: 
    #        print(st['properties']['STATE_NAME'])        
            if st['properties']['STATE_NAME'] == row['state']:
    #            print(st['properties']['STATE_NAME'],',',row['state'])
                st['properties']['angry_value'] = row['angry_value']
                st['properties']['median_income'] = row['income']
                st['properties']['unemployment_rate'] = row['unemploy_rate']
                st['properties']['labor_force_median_age'] = row['median_age']
                st['properties']['tweets_number'] = row['Number of Tweets']

    #pprint(st)
    with open('forFrontEndState.json', 'w') as outfile:
        json.dump(state, outfile)
    return state
    
def save2_couchdb(server,finalgjson,name):
    
    couchserver = couchdb.Server(server)
    
    geodb = name
    if geodb in couchserver:
        del couchserver[geodb]
        gdb = couchserver.create(geodb)
    else:
        gdb = couchserver.create(geodb)
        
    gdb.save(finalgjson)


def main():

    From_add = "http://admin:nmsl@172.26.38.7:5984/"
    From_dbname = 'tweet'
    To_server = "http://admin:nmsl@172.26.38.7:5984/"
    To_state_dbname = 'state_resultdb'
    To_city_dbname = 'city_resultdb'

    db=connect_couchdb(From_add,From_dbname)
    angryDF = angry_calculation(db)

    finalDF = angry_dataFrame(angryDF)
    Punish_finalDF =punisher_NumTweet(finalDF)
    normalized_sepCityDF = angValue_normalization(Punish_finalDF)

    #load and process aurin data -- cit level
    age = pd.read_csv("age.csv")
    age = age.loc[age.sa2_name16.isin(list(normalized_sepCityDF['city'])),:]
    income = pd.read_csv("income.csv")
    income = income.loc[income.sa2_name16.isin(list(normalized_sepCityDF['city'])),:]
    unemployment = pd.read_csv('unemployment.csv')
    aurinDF = age.merge(income, on = 'sa2_name16', how = 'inner')
    aurinDF.rename(columns={'sa2_name16':'city'}, inplace=True)
    aurinDFF = pd.merge(aurinDF, unemployment,how = 'outer', on = 'city')

    #retulst for city 

    #load geojson format for the front end
    with open('au_cities_60.geojson') as ct:
        city = json.load(ct)
    #combine aurin data with sentiment result    
    sentiment_aurin = sentiment_merge_aurin(normalized_sepCityDF,aurinDFF)
    #generate geojson result and save to local
    city_result = generate_geojson_state_city(sentiment_aurin,city)
    #send geojson to server 
    save2_couchdb(To_server,city_result,To_city_dbname)

    #result for state

    #load geojson format for the front end
    with open('aus_states.geojson') as st:
        state = json.load(st)
    #summary city data to state level    
    state_sum = state_summary(normalized_sepCityDF)
    #set 0 to 1.5 so that this area is not black at the front end
    state_sum.loc[state_sum['angry_value'] == 0,'angry_value'] = 1.5

    #combine aurin data with sentiment result    
    state_sum_aurin = state_combine_aurin(state_sum,auData)
    #generate geojson result and save to local
    state_result = generate_geojson(state_sum_aurin,state)
    #send geojson to server 
    save2_couchdb(To_server,state_result,To_state_dbname)

if __name__ = "__main__":
    main();