from flask import Flask

app = Flask(__name__)
# server = Server('http://115.146.95.246:5984')
# db = server['twitter_rest']

# import view_db.couchdb
from app import model
from app import controller
