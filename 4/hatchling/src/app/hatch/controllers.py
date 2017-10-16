from flask import request, jsonify
# All hatch-specific imports
from app.hatch import hatch
import daos # pylint: disable=W0403
from models import * # pylint: disable=W0403

# Serializer: for each chirp c returned, call the following:
# chirp_schema.dump(c).data => dictionary representation of the chirp
chirp_schema = ChirpSchema()

@hatch.route('/chirps/create/', methods=['POST'])
def create_chirp():
  """
  Endpoint to create a chirp
  """
  # Grab information from the request
  content = request.args.get('content') # url param
  author = request.args.get('author', None) # url param

  # Create the chirp
  chirp = daos.create_chirp(content=content, author=author)

  # Respond to the request w/a JSON
  return jsonify({'chirp': chirp_schema.dump(chirp).data})

@hatch.route('/chirps/', methods=['GET'])
def get_chirps():
  """
  Endpoint to get chirps (descending order by date, paginated)
  """
  # Grab information from the request
  page = int(request.args.get('page')) # url param
  page_size = int(request.args.get('page_size')) # url param

  # Get the chirps
  chirps = daos.get_chirps(page, page_size)

  # Respond to the request w/a JSON
  return jsonify({'chirps': [chirp_schema.dump(c).data for c in chirps]})
