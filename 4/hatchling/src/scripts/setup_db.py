#!/usr/bin/python
import sys
import os
import shutil

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

# This file is a script to run in order to
# setup the MySQL DB every time there's a
# fundamental change in the data

def setup_dbs():
  print 'Setting up databases...'
  os.chdir('..')
  # Run commands to mount the DB + migrate
  os.system('python manage.py db init')
  os.system('python manage.py db migrate')
  os.system('python manage.py db upgrade')
  os.chdir('scripts')
  print 'Finished setting up databases...'

def reset_migrations():
  try:
    os.chdir('..')
    shutil.rmtree('migrations')
    os.system('mysql --user={} --password={} {} '
      .format(os.environ['HATCH_DB_USER'],
              os.environ['HATCH_DB_PASS'],
              os.environ['HATCH_DB_NAME'])
        + '-e "drop table alembic_version"')
    os.chdir('scripts')
    print 'Migrations folder deleted...'
  except OSError:
    os.chdir('scripts')
    print 'No migrations folder to delete...'

if __name__ == '__main__':
  reset_migrations()
  setup_dbs()
