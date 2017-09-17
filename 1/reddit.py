import requests
from termcolor import colored

def print_request_metadata(r, title):
  # Print out request information
  top_phrase = '---------- {} Metadata ----------'.format(title)
  print top_phrase
  # Headers
  print 'Headers: '
  for h in r.headers:
    length_limit = 33
    # Clean up header display
    beautified_header = r.headers[h] \
      if len(r.headers[h]) < length_limit \
      else r.headers[h][:length_limit - 3] + ' ...'
    print '  {}{} {}'.format(
        colored(h, 'white'),
        colored(':', 'white'),
        colored(beautified_header, 'cyan')
    )
  # URL
  print colored('URL:', 'white'), colored(r.url, 'cyan')
  print '-' * len(top_phrase)
  print

# NOTE - main function
def get_reddit_posts(uri):
  # Ensure proper format
  if '.json' not in uri:
    uri = uri + '.json'

  # Spoofs that a request is being made
  # from a browser
  headers = {
      'User-Agent':
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 ' + \
      '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
  }

  # NOTE - HTTP request made here
  r = requests.get(uri, headers=headers)

  # Print out metadata
  print_request_metadata(r.request, 'Request')
  print_request_metadata(r, 'Response')

  # Print out the top titles
  print 'Top 10 Front Page Titles:'
  r_json = r.json()
  for i, element in enumerate(r_json['data']['children'][:10]):
    print '{}. {}'.format(i+1, element['data']['title'].encode('utf-8'))
    # print '- By \'{}\''.format(element['data']['author'].encode('utf-8'))
    # print '- URL: {}'.format(element['data']['url'].encode('utf-8'))
    # TODO - grab more information to display if you want!
  print

if __name__ == '__main__':
  while True:
    reddit_url = raw_input('Type the URL of a subreddit:\n')
    get_reddit_posts(reddit_url)
