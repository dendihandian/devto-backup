import logging
import requests
import json

# set the logging level
logging.basicConfig(level=logging.DEBUG)

# build params for the request
params = {
    'username': 'dendihandian'
}
logging.debug(f'params: {json.dumps(params)}')


# perform request
logging.info('requesting...')
result = requests.get('https://dev.to/api/articles', params=params)
logging.info('...done')

articles = result.json()
for article in articles:
    print(article['title'])

print(result.status_code)