#
# Complete the 'getArticleTitles' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING author as parameter.
#
import json
import requests

def getArticleTitles(author):
    # Write your code here
    url = 'https://jsonmock.hackerrank.com/api/articles?author='

    response = requests.get(url + author)
    data = response.json()
    total_page = data['total_pages']
    per_page = data['per_page']
    titles = []

    for page in range(1, total_page + 1):
        content = requests.get(url + '{}&page={}'.format(author, page)).json()
        
        if total_page > 1 and total_page - page > 0:
            nav_range = per_page
        elif total_page > 1 and total_page - page == 0:
            nav_range = content['total'] - per_page * (page - 1)
        else:
            nav_range = content['total']

        for per_p in range(nav_range):
            title = content['data'][per_p]['title']
            story_title = content['data'][per_p]['story_title']
            if not title and not story_title:
                continue
            elif title:
                titles.append(title)
            else:
                titles.append(story_title)

    return titles
    
if __name__ == '__main__':
    titles = getArticleTitles('coloneltcb')
    #titles = getArticleTitles('epaga')
    print(titles)
    #print(sorted(titles))
