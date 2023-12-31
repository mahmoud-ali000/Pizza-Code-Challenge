from flask import Flask
from flask_restful import Api 
from flask_migrate import Migrate
from api.models import db

app = Flask(__name__)
api = Api(app)


app.config['SECRET_KEY'] = 'f9bf78b9a18ce6d46a0cd2b0b86df9da'
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///project.db"

migrate = Migrate(app, db)
db.init_app(app)

from api import routes
























