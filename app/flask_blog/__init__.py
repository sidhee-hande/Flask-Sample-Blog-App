from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app= Flask(__name__)


app.config.from_object('flask_blog.config')

db=SQLAlchemy(app)
migrate = Migrate(app, db)
from flask_blog.views import views, entries