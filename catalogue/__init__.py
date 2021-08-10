import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalogue.db'
app.config.update(SECRET_KEY=os.urandom(24))
db = SQLAlchemy(app)

# Upload folder
UPLOAD_FOLDER = r'C:\Users\Usuario\Proyectos\cs50\catalogue\catalogue\static\files' #Check on production
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

from catalogue import routes, admin