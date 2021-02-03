import requests
import json

def get_movie_titles(substr):
    url = 'https://jsonmock.hackerrank.com/api/movies/search/?Title='

    response = requests.get(url)
    data = response.json()
    total_page = data['total_pages']
    per_page = data['per_page']
    titles = []

    for page in range(1, total_page + 1):
        content = requests.get('https://jsonmock.hackerrank.com/api/movies/search/?Title={}&page={}'.format(substr,page)).json()
        if content['data']:
            for row in content['data']:
                print(row['Title'])

if __name__ == '__main__':
    get_movie_titles('spiderman')
