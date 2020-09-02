from flask import Flask
from config import Config

app = Flask(__name__)
# Import the config
app.config.from_object(Config)

from app import routes
