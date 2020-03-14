""" Whole body of the program, executes just about everything. """
import json
import requests
import markdown
from flask import Flask

# pylint: disable=consider-using-enumerate

API_LINK = "https://api.jikan.moe/v3/"

class Anime:
    """ Simple class for containing anime info
    """
    def __init__(self, name, episodes, rating):
        """ Constructor
        """
        self.name = name
        self.episodes = episodes
        self.rating = rating

    def get_anime(self):
        """ get this. anime info
        """
        return {self.name, self.episodes, self.rating}

    def print(self):
        """ print anime info
        """
        # pylint: disable=line-too-long
        print("Name: " + self.name + "\nEpisodes: " + self.episodes + "\nRating: " + self.rating + "\n\n\n")

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
    # pylint: disable=singleton-comparison
    if res["airing"] == True:
        is_airing = "Is Airing: Yes"
    return anime_name + "\n" + episodes + "\n" + is_airing + "\n" + score + "\n" + description

def get_top_anime(page_num):
    """
        Get top anime by page.
        page = 50 animes
    """
    top_anime = []
    res = requests.get(API_LINK + "top/anime/" + str(page_num) + "/?page=" + str(page_num))
    if res.status_code != 200:
        return "error"
    res = json.loads(res.text)["top"]

    for i in range(len(res)):
        top_anime.append(Anime(res[i]["title"], str(res[i]["episodes"]), str(res[i]["score"])))

    return top_anime

#res = requests.get(GetAnimeByName("One Piece"))
#

def main():
    """ Main Function """
    top = get_top_anime(1)
    if top == "error":
        print(top)
    else:
        for i in range(len(top)):
            top[i].print()

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
