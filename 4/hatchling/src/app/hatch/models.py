from app import db # Grab the db from the top-level app
from marshmallow_sqlalchemy import ModelSchema

# Models describe the data.  Models can be plain old Python classes
# or, in the case, have some association with the database.

class Base(db.Model):
  """
  The parent of all models - keeps track of fundamental
  timestamp information (created_at / updated_at)
  """
  __abstract__ = True
  created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
  updated_at = db.Column(
      db.DateTime,
      default=db.func.current_timestamp(),
      onupdate=db.func.current_timestamp())

class Chirp(Base):
  """
  An anonymous micro-blog post limited to 140 characters
  """
  __tablename__ = 'chirps'

  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String(140), nullable=False)
  author = db.Column(db.String(255), nullable=True)

  def __init__(self, **kwargs):
    self.content = kwargs.get('content')
    self.author = kwargs.get('author', None)

class ChirpSchema(ModelSchema):
  """
  Serializer class to convert a Chrip model into a dictionary
  """
  class Meta(ModelSchema.Meta):
    model = Chirp
