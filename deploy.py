""" Whole body of the program, executes just about everything. """
import json
import requests
import markdown
from flask import Flask

API_LINK = "https://api.jikan.moe/v3/"


def get_api_link():
    """ Pass the api link to unit-tests """
    return API_LINK


def get_anime_by_name(name):
    """
        Using the api link provided by jikan, we manipulate the url to get the anime's
        information from MAL
     """
    res = requests.get(API_LINK + "search/anime?q=" + name + "&page=1")
    res = json.loads(res.text)["results"][0]
    is_airing = "Is Airing: No"
    score = "Score: " + str(res["score"])
    description = "Description: " + res["synopsis"]
    episodes = "Episodes: " + str(res["episodes"])
    anime_name = "Name: " + res["title"]
    if res["airing"] == True:
        is_airing = "Is Airing: Yes"
    return anime_name + "\n" + episodes + "\n" + is_airing + "\n" + score + "\n" + description


#res = requests.get(GetAnimeByName("One Piece"))
#

def main():
    """ Main Function """
    print(get_anime_by_name("made in abyss"))


if __name__ == '__main__':
    main()

# pylint: disable=invalid-name
app = Flask(__name__)

@app.route('/')
def index():
    """Readme to html"""
    file = open('README.md', 'r')
    html = markdown.markdown(file.read())
    #print(html)
    return html
