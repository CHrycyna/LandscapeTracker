import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import basedir
import wtforms_json

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config['SECRET_KEY']
db = SQLAlchemy(app)

from app import views