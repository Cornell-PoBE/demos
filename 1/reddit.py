import requests

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

  r = requests.get(uri, headers=headers)

  # Print out request information
  top_phrase = '------ Request Metadata ------'
  print top_phrase
  print r.request.headers
  print '-' * len(top_phrase)
  print

  # Print out the top titles
  print 'Top 10 Front Page Titles:'
  r_json = r.json()
  for i, element in enumerate(r_json['data']['children'][:10]):
    print '{}. {}'.format(i+1, element['data']['title'])
  print

if __name__ == '__main__':
  while True:
    reddit_url = raw_input('Type the URL of a subreddit:\n')
    get_reddit_posts(reddit_url)
