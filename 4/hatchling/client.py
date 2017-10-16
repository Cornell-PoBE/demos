#!/usr/bin/python
import urllib
import requests # for making HTTP requests

BASE_URI = 'http://127.0.0.1:5000/api/v1/chirps'

def chirp_to_string(chirp):
  return 'Chirp: \'{}\' by \'{}\''.format(chirp['content'], chirp['author'])

def create_chirp(**kwargs):
  content = kwargs.get('content')
  author = kwargs.get('author')
  params = dict()
  params['content'] = content
  if author:
    params['author'] = author
  encoded_params = urllib.urlencode(params)

  response = requests.\
    post('{}/create/?{}'.format(BASE_URI, encoded_params)).\
    json()

  return chirp_to_string(response['chirp'])

def get_chirps(**kwargs):
  page = kwargs.get('page', 0)
  page_size = kwargs.get('page_size', 10)
  params = {'page': page, 'page_size': page_size}
  encoded_params = urllib.urlencode(params)

  response = requests.\
    get('{}/?{}'.format(BASE_URI, encoded_params)).\
    json()

  return '\n'.join(chirp_to_string(c) for c in response['chirps'])

# REPL runnable
if __name__ == '__main__':
  prompt = 'Type in a command, either:\n' + \
  'CREATE content:<content> author:<author>\n' + \
  'GET page:<page> page_size:<page_size>'
  print prompt
  while True:
    try:
      command = raw_input()
      command_phrase = command[:command.index(' ')]
      if command_phrase == 'CREATE':
        content_i = command.index('content:')
        author_i = command.index('author:')
        content = command[content_i+len('content:'):author_i].strip()
        author = command[author_i+len('author:'):].strip()
        print create_chirp(content=content, author=author)
      elif command_phrase == 'GET':
        page_i = command.index('page:')
        page_size_i = command.index('page_size:')
        page = int(command[page_i+len('page:'):page_size_i].strip())
        page_size = int(command[page_size_i+len('page_size:'):].strip())
        print get_chirps(page=page, page_size=page_size)
      else:
        raise Exception()
    except Exception:
      print 'Invalid command, try again!'
