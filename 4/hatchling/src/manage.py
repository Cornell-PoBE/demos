import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db

# Utility script allowing direct access to
# database migration (init, migrate, upgrade)
# functionality

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()
