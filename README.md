### COMP90024 Project 2: Negative Sentiment Analysis Based on Tweets in Australia

This is the Project 2 for COMP90024 (Cluster and Cloud Computing) from the University of Melbourne.

In this project, four virtual machines (Ubuntu) were built on the [Nectar](https://nectar.org.au/) cloud platform, three of which deployed [CouchDB](http://couchdb.apache.org/) distributed databases and one deployed the [Flask](http://flask.palletsprojects.com/en/1.1.x/)-based Web backend, using [Ansible](https://www.ansible.com/) for automated deployment. Climb the Tweets posted in Australia over a period of time, store them into CouchDB, use the relevant Python libraries for sentiment analysis, and visualize the front end of the results.

The 

#### 1. What is the task?
The focus of this project is to explore the [Seven Deadly Sins](https://en.wikipedia.org/wiki/Seven_deadly_sins) through social media analytics. There has been a huge amount of work on sentiment analysis of social media, e.g. are people happy or sad as recorded by their tweets, but far less work on other aspects of human nature and emotion: greed, lust, laziness etc. A few examples of the deadly sins might be:

* **Pride**: how many selfies are taken in particular areas, how many tweets/images about make-up/personal care, …
* **Greed**: tweets/images about food/drink or about money/income, …
* **Lust**: tweets that include the likes of “I want…”, “I love…”, “I’m jealous…” or images of a “certain” adult nature;
* **Envy**: tweets that include the likes of “I wish…”, “I need…”, “I desire…”
* **Gluttony**: tweets/images that show overweight people or about dietary issues, e.g. fast food restaurants such as #maccas or related products such as #bigmac etc;
* **Wrath**: tweets that include the likes of “I hate…”, “I’m angry…” or about crime or areas with high levels of negative emotion (sentiment) on particular topics etc
* **Sloth**: tweets that mention sleep, laziness, or areas where there are more/less tweets at night/early morning.

The goal of the project is to harvest tweets from across the cities of Australia on the UniMelb Research Cloud and undertake a variety of data analytics scenarios that tell interesting stories of life in Australian cities related to one or more deadly sins and importantly how the Twitter and precollected Instagram data can be used alongside/compared with/augment the data available within the [AURIN](https://aurin.org.au/) platform to assess/validate these sins.


WebServer - webserver built by flask + uWSGI

Automation - ansible + python script for auto environment deployment

Data_analysis - data analysis module for "Seven Deadly Sins"

Harvest - crawler for Twitter in Australia

CouchDB - CouchDB cluster and map-reduce