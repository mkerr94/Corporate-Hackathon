from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, template_folder='templates')

# Configurations
app.config.from_object('config')
db = SQLAlchemy(app)

from app.myModule.controllers import myModule
app.register_blueprint(myModule)

db.create_all()


from app.myModule.models import Comment, Vote, Post, Category

