
from flask import Flask,g
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key='daiker666'
app.config.from_object('config')
db = SQLAlchemy(app)
from app import views,models