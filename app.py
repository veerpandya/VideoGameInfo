from flask import Flask, request, render_template
from hltb import hltb_info
from metacritic import metascore
from wiki import wiki_info
from google import get_release
import requests

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


# Search for the input game title
@app.route('/search')
def search():
    # Get the search query
    query = request.args.get("query")

    # Get HLTB data
    game_data = hltb_info(query)

    # Get the rest of the game info
    for game in game_data:
        game["platforms"], game["genre"] = wiki_info(game["name"])
        game["release"] = get_release(game["name"])
        (
            game["critic"],
            game["ccolor"],
            game["user"],
            game["ucolor"]
            ) = metascore(game["name"])

    context = {
        "game_data": game_data,
        "query": query
    }

    return render_template('results.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
