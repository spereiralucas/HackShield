import os
from flask import Flask
from flask_cors import CORS
from constants import constants
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint


swagger_ui_blueprint = get_swaggerui_blueprint(
    constants['SWAGGER_URL'],
    constants['API_URL'],
    config={'app_name': 'Access API'}
)

app = Flask(
    __name__,
    template_folder='views',
    static_folder='views/static/'
)
app.app_context().push
CORS(app)

app.config.from_object('config')
app.register_blueprint(
    swagger_ui_blueprint,
    url_prefix=constants['SWAGGER_URL']
)

os.environ['WERKZEUG_TIMEOUT'] = '60'

db = SQLAlchemy(app)

migrate = Migrate(app, db)

# Import Models
from app.models import __init__

# Import Routes
from app.routes import __init__
