from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"]='b4476a91f0f2670aacabb899647dc6f5'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///getpro.db"

base = SQLAlchemy(app)

from getpro import routes



