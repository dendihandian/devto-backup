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

# process each article
username = params['username']
posts_path = os.path.join(sys.path[0], 'dev.to', username, 'posts')

if not os.path.exists(posts_path):
    os.makedirs(posts_path)

for article in articles:
    # print(article['title'])
    slug = article['slug']
    filename = f'{slug}.md'
    # open(f'dev.to/{username}/posts/{filename}', "w+").close()
    open(os.path.join(posts_path, filename), "w+").close()

# print(os.path.join(sys.path[0], "my_file.txt"))