from pprint import pprint

from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
movie_titles = [movie.text for movie in soup.find_all(name='h3')]
pprint(movie_titles)

try:
    with open('movies.txt', 'w') as file:
        for number in range(len(movie_titles) - 1, -1, -1):
            print(movie_titles[number])
            file.write(f"{movie_titles[number]}\n")
except FileNotFoundError:
    print("The 'list' directory does not exist")
