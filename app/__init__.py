from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.secret_key = 'stock application by shubham '

from app.models import *