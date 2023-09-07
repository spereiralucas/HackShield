from flask import Flask
from constants import constants
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(
    __name__,
    template_folder='views',
    static_folder='views/static/'
)
app.app_context().push

app.config.from_object('config')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

# Import Models
from app.models import __init__

# Import Routes
from app.routes import __init__
