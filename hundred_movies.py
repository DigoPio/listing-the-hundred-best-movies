import requests
from bs4 import BeautifulSoup

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')

soup = BeautifulSoup(response.text, 'html.parser')


movies_title = soup.find_all('h3', class_='title')


titles = [title.getText() for title in movies_title]


for movie in titles[::-1]:
    with open('moves.txt', mode='a') as file:
        file.write(f'{movie}\n')



