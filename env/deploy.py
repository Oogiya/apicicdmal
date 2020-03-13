from jikanpy import Jikan
import requests
import json
from flask import Flask

api_link = "https://api.jikan.moe/v3/"

# TODO
# 1 - Get anime by name
# english name, status, episodes, aired, source, studio, score, ranked

# 2 - Get top anime
# 3 - get top by genre

def GetAnimeByName(name):
    res = requests.get(api_link + "search/anime?q=" + name + "&page=1")
    res = json.loads(res.text)["results"][0]
    return "Name: " + res["title"] + "\nEpisodes: " + str(res["episodes"])


#res = requests.get(GetAnimeByName("One Piece"))
#
print(GetAnimeByName("Made In Abyss"))

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Yes</h1>'