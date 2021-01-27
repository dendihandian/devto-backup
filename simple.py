import requests
import os
import sys

# build params for the request
params = {
    'username': 'dendihandian'
}

# perform request
result = requests.get('https://dev.to/api/articles', params=params)
articles = result.json()


# make directories for posts if not exists
username = params['username']
posts_path = os.path.join(sys.path[0], 'dev.to', username, 'posts')
if not os.path.exists(posts_path):
    os.makedirs(posts_path)

# process each article
for article in articles:
    slug = article['slug']
    article_id = article['id']
    filename = f'{slug}.md'
    article_result = requests.get(f'https://dev.to/api/articles/{article_id}')
    article = article_result.json()
    f = open(os.path.join(posts_path, filename), "w+", encoding="utf-8")
    f.write(article['body_markdown'])
    f.close()
