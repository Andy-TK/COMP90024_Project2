### COMP90024 Project 2: Negative Sentiment Analysis Based on Tweets in Australia

This is the Project 2 for COMP90024 (Cluster and Cloud Computing) from the University of Melbourne.

In this project, four virtual machines (Ubuntu) were built on the [Nectar](https://nectar.org.au/) cloud platform, three of which deployed [CouchDB](http://couchdb.apache.org/) distributed databases and one deployed the [Flask](http://flask.palletsprojects.com/en/1.1.x/)-based Web backend, using [Ansible](https://www.ansible.com/) for automated deployment. Climb the Tweets posted in Australia over a period of time, store them into CouchDB, use the relevant Python libraries for sentiment analysis, and visualize the front end of the results. For more details, please check the [project specifications](https://github.com/Andy-TK/COMP90024_Project2/blob/master/project%20specifications.pdf) and [project report](https://github.com/Andy-TK/COMP90024_Project2/blob/master/CCC-Team35-Report.pdf).

The architecture is shown as below:
<img src="https://github.com/Andy-TK/COMP90024_Project2/blob/master/images/architecture.png" alt="architecture" width="50%">

The website demo is shown as below:
<img src="https://github.com/Andy-TK/COMP90024_Project2/blob/master/images/00_home.png" alt="homepage" width="50%">

<img src="https://github.com/Andy-TK/COMP90024_Project2/blob/master/images/01_team.png" alt="team" width="50%">

<img src="https://github.com/Andy-TK/COMP90024_Project2/blob/master/images/03_work1.png" alt="map_01" width="50%">

<img src="https://github.com/Andy-TK/COMP90024_Project2/blob/master/images/04_work2.png" alt="graph_01" width="50%">

The video demo is avaiable on my [YouTube](https://www.youtube.com/watch?v=4vs__dmppZg).

The 


WebServer - webserver built by flask + uWSGI

Automation - ansible + python script for auto environment deployment

Data_analysis - data analysis module for "Seven Deadly Sins"

Harvest - crawler for Twitter in Australia

CouchDB - CouchDB cluster and map-reduce