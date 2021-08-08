from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalogue.db'
db = SQLAlchemy(app)

# Upload folder
UPLOAD_FOLDER = 'static/files'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

from catalogue import routes
