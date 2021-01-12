import requests
from bs4 import BeautifulSoup as bs


# Gets game rating score from metacritic.com
def metascore(name):

    # User Agent needed to access the site
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
               " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88"
               " Safari/537.36"}

    baseURL = "https://www.metacritic.com/game/"

    # Makes new url for the game
    gameURL = baseURL + platform.lower() + "/" + name.lower()

    # Load the webpage content
    r = requests.get(gameURL, headers=headers)

    # Convert to a beautiful soup object
    soup = bs(r.content, "html5lib")

    # Sets up dictionary of scores
    scores = {"critic": "N/A", "user": "N/A"}
    # Using try to prevent errors if the page or game is not found
    try:
        scores["critic"] = soup.find(class_="metascore_w").text
        scores["user"] = soup.find(class_="user").text
    except Exception:
        scores = {"critic": "N/A", "user": "N/A"}

    # Returns scores
    return(scores)
