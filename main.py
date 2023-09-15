import os
from flask import Flask, render_template, request, url_for, redirect
from routes.usuario import usuario
from utils.db import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.secret_key = 'millavesecreta'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(usuario)
SQLAlchemy(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)