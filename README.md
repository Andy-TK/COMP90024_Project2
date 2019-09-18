### COMP90024 Project 2: Negative Sentiment Analysis Based on Tweets in Australia

This is the Project 2 for COMP90024 (Cluster and Cloud Computing) from the University of Melbourne. 

The goal of this project is to harvest tweets from across the cities of Australia on the [UniMelb Research Cloud](https://research.unimelb.edu.au/infrastructure/research-platform-services/services/research-cloud) and undertake a variety of data analytics scenarios that tell interesting stories of life in Australian cities related to one or more [deadly sins](https://en.wikipedia.org/wiki/Seven_deadly_sins) and importantly how the Twitter and precollected Instagram data can be used alongside/compared with/augment the data available within the [AURIN](https://aurin.org.au/) platform to assess/validate these sins. 

For more details, please check the [project specifications](https://github.com/Andy-TK/COMP90024_Project2/blob/master/project%20specifications.pdf) and [project report](https://github.com/Andy-TK/COMP90024_Project2/blob/master/CCC-Team35-Report.pdf).

#### 1. The Architecture and Website Demo
In this project, four virtual machines (Ubuntu) were built on the [Nectar](https://nectar.org.au/) cloud platform, three of which deployed [CouchDB](http://couchdb.apache.org/) distributed databases and one deployed the [Flask](http://flask.palletsprojects.com/en/1.1.x/)-based Web backend, using [Ansible](https://www.ansible.com/) for automated deployment. Climb the Tweets posted in Australia over a period of time, store them into CouchDB, use the relevant Python libraries for sentiment analysis, and visualize the front end of the results.

**1.1. The architecture is shown as below:**

<img src="https://github.com/Andy-TK/COMP90024_Project2/blob/master/images/architecture.png" alt="architecture" width="50%">

**1.2. The website demo is shown as below:**

<img src="https://github.com/Andy-TK/COMP90024_Project2/blob/master/images/00_home.png" alt="homepage" width="70%">

<img src="https://github.com/Andy-TK/COMP90024_Project2/blob/master/images/01_team.png" alt="team" width="70%">

<img src="https://github.com/Andy-TK/COMP90024_Project2/blob/master/images/03_work1.png" alt="map_01" width="70%">

<img src="https://github.com/Andy-TK/COMP90024_Project2/blob/master/images/04_work2.png" alt="graph_01" width="70%">

The video demo is avaiable on my [YouTube](https://www.youtube.com/watch?v=4vs__dmppZg).

#### 2. Some Relevant Technology Stacks

* **WebServer** - webserver built by [Flask](http://flask.palletsprojects.com/en/1.1.x/) + [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)

* **Automation** - [Ansible playbook](https://www.ansible.com/) + [Automation.py](https://github.com/Andy-TK/COMP90024_Project2/blob/master/Automation/Automation.py) for auto environment deployment (an alternative option is [Docker](https://www.docker.com/))

* **Harvest** - crawler for Twitter in Australia

* **CouchDB** - [CouchDB](http://couchdb.apache.org/) cluster and [Map-Reduce](https://docs.couchdb.org/en/stable/ddocs/views/intro.html)

* **Data Analysis** - a _Python module_ [reactionrnn](https://pypi.org/project/reactionrnn/) for sentiment analysis

* **Data Visualization** - [GeoJSON](https://geojson.org/) files + [Mapbox](https://www.mapbox.com/) for map function and [Highcharts](https://www.highcharts.com/) for graphs function

* **Website** - Based on _HTML5_, _CSS3_ and _JavaScript_. Template is provided by [templatemag.com](https://templatemag.com/)

