from flask import Flask, request, render_template
from hltb import hltb_info
import metacritic
import wiki
import google
import requests

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


# Search for the input game title
@app.route('/search')
def search():

    query = request.args.get("query")

    games = hltb_info(query)

    context = {
        "games": games
    }

    return render_template('results.html', **context)






if __name__ == '__main__':
    app.run(debug=True)
