from app.hatch.models import *
import app.utils as utils

# A series of functions that perform fundamental, high-level
# queries / mutations on the data.  Files of this type are
# important, as they link the view (controller) layer to the
# DB layer of the application

def create_chirp(**kwargs):
  content = kwargs.get('content')
  author = kwargs.get('author', None)

  # Rather than INSERT INTO <table> (<columns>) VALUES (<values>),
  # the creation of an instance of the model, followed by a 'commit'
  # to the database is all you need
  new_chirp = Chirp(content=content, author=author)
  return utils.commit_model(new_chirp)

def delete_chirp(chirp_id):
  # Equivalent to: 'SELECT * FROM chirps WHERE id = {chirp_id}'
  optional_chirp = Chirp.query.get(chirp_id)

  if not optional_chirp:
    raise Exception('A chirp does not exist with said ID!')

  return utils.delete_model(optional_chirp)

def get_chirps_from_dates(start_date, end_date):
  pass

def get_chirps(page, page_size):
  pass
