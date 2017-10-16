from flask import Blueprint
from app import *

# Setup the Blueprint (series of operations +
# functionality that stays packaged together)
# http://flask.pocoo.org/docs/0.12/blueprints/
hatch = Blueprint('hatch', __name__, url_prefix='/api/v1')

# Import all models
from app.hatch.models import *

# Import all controllers
from app.hatch.controllers import *
