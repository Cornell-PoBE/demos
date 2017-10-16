from app.hatch.models import *
import app.utils as utils

# A series of functions that perform fundamental, high-level
# queries / mutations on the data.  Files of this type are
# important, as they link the view (controller) layer to the
# DB layer of the application

# NOTE - not all of these are used in the app, but are written
# for the sake of example.  If you clone or fork this repo, feel
# free to write more / play around with different types of data-accesses
# and mutations!

def create_chirp(**kwargs):
  content = kwargs.get('content')
  author = kwargs.get('author', None)

  # Rather than INSERT INTO <table> (<columns>) VALUES (<values>),
  # the creation of an instance of the model, followed by a 'commit'
  # to the database is all you need
  new_chirp = Chirp(content=content, author=author)
  return utils.commit_model(new_chirp)

def delete_chirp(chirp_id):
  # Equivalent to:
  # SELECT *
  # FROM chirps
  # WHERE id = {chirp_id}
  optional_chirp = Chirp.query.get(chirp_id)

  if not optional_chirp:
    raise Exception('A chirp does not exist with said ID!')

  return utils.delete_model(optional_chirp)

def get_chirps_from_dates(start_date, end_date):
  # Equivalent to:
  # SELECT *
  # FROM chirps
  # WHERE created_at >= {start_date} AND created_at <= {end_date}
  return Chirp.query.\
    filter(Chrip.created_at >= start_date, Chirp.created_at <= end_date).\
    all()

def get_chirps(page, page_size):
  # Paginates the chirps, so we aren't reading the entire DB;
  # equivalent to:
  # SELECT *
  # FROM chirps
  # ORDER BY created_at DESC
  # LIMIT {page_size} OFFSET {page_size * page}
  return Chirp.\
    query.\
    order_by(Chirp.created_at.desc()).\
    limit(page_size).\
    offset(page * page_size).all()
