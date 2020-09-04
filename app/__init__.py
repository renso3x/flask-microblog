from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
# Import the config
app.config.from_object(Config)
# SQL Alchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
