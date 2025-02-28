from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI", "fallback_key")
    db.init_app(app)
    return app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv("DATABASE_URI", "fallback_key")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']=os.getenv("SECRET_KEY", "fallback_key")

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.views import *
from app.models import *