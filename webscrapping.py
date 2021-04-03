from bs4 import BeautifulSoup
import requests

sorce_code = requests.get('https://www.iashyam.in/').text

soup = BeautifulSoup(sorce_code, 'lxml')


articles = soup.find_all('article')

def get_things(article):
    try:
        title = article.find('h3', class_='post-title').text
    except:
        title='Untitled'
    summary = article.find('div', class_="snippet-item").text
    link = article.find('a', class_='snippet-fade')['href']

    return title, summary, link

with open('Blog.txt','w') as file:
    for article in articles:
        title, summary, link = get_things(article)

        file.write(title)
        file.write(summary)
        file.write(link)
        file.write('\n')


