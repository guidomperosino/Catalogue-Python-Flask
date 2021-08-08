from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalogue.db'
db = SQLAlchemy(app)

# Upload folder
UPLOAD_FOLDER = r'C:\Users\Usuario\Proyectos\cs50\catalogue\catalogue\static\files' #Check on production
ALLOWED_EXTENSIONS = {'csv'} #Revisar tiene que ser global
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

from catalogue import routes
