from flask import Flask, request, render_template
from hltb import hltb_info
from metacritic import metascore
from wiki import wiki_info
from google import get_release
import requests
from multiprocessing import Process, Queue

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

    # List of processes for multiprocessing
    processes = []

    # Queue for processes
    q = Queue()

    # Add each game to its own process to get info simultaneously
    for game in game_data:
        processes.append(Process(target=get_info, args=(game, q)))

    # Start the processes
    for p in processes:
        p.start()

    # Wait for the processes to finish
    for p in processes:
        p.join()

    # Get info from the queue
    for i in range(len(game_data)):
        game_data[i] = q.get()

    # Reversing list of games to show games with most info first
    game_data.reverse()

    context = {
        "game_data": game_data,
        "query": query
    }

    return render_template('results.html', **context)


# Helper that converts each search for a game into a process
def get_info(game, q):
    game["platforms"], game["genre"] = wiki_info(game["name"])
    game["release"] = get_release(game["name"])
    (
        game["critic"],
        game["ccolor"],
        game["user"],
        game["ucolor"]
        ) = metascore(game["name"])

    q.put(game)


if __name__ == '__main__':
    app.run(debug=True)
