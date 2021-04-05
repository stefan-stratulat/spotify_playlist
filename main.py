import requests
from bs4 import BeautifulSoup
import lxml

# promt = input("Which year would you like to travel to? Type the date in this format YYYY-MM-DD: ")
# print(promt)

promt = "2009-10-03"

URL = "https://www.billboard.com/charts/hot-100/"

response = requests.get(f"{URL}{promt}")

soup = BeautifulSoup(response.text, "lxml")

all_ranks = soup.find_all("span", class_="chart-element__rank__number")
song_ranks = [rank.getText() for rank in all_ranks]

all_names = soup.find_all("span", class_="chart-element__information__song text--truncate color--primary")
song_names = [name.getText() for name in all_names]


all_artists = soup.find_all("span", class_="chart-element__information__artist text--truncate color--secondary")
song_artists = [artist.getText() for artist in all_artists]
print(song_artists)
