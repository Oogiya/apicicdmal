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
    return "Name: " + res["title"] + "\nEpisodes: " + str(res["episodes"])


#res = requests.get(GetAnimeByName("One Piece"))
#

def main():
    """ Main Function """



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
