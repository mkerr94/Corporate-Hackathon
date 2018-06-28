from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql2245027:hR8*eV4!@sql2.freemysqlhosting.net/sql2245027'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config.from_object('config')
db = SQLAlchemy(app)

from app.myModule.controllers import myModule
app.register_blueprint(myModule)

db.create_all()
