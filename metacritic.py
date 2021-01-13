import requests
from bs4 import BeautifulSoup as bs


# Gets game rating score from metacritic.com
def metascore(name):

    # User Agent needed to access the site
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
               " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88"
               " Safari/537.36"}

    baseURL = "https://www.metacritic.com"

    # Gets rid of year from name to work with metacritic's search
    name = name.split("(")[0]

    nameURL = name.replace(" ", "%20")

    # Makes new url for the search results
    searchURL = baseURL + "/search/game/" + name + "/results?sort=score"

    # Load the webpage content
    r = requests.get(searchURL, headers=headers)

    # Convert to a beautiful soup object
    soup = bs(r.content, "lxml")

    # Using try to prevent errors if the page or game is not found
    try:
        # Gets the url for the game from the search results
        gameURL = baseURL + soup.find(
                                    "li", class_="first_result"
                                    ).find("a")["href"]

        # Load new page for the specific game
        r = requests.get(gameURL, headers=headers)
        soup = bs(r.content, "lxml")
        # Get the scores
        critic = soup.find(class_="xlarge").text
        if float(critic) < 5:
            ccolor = "bad"
        elif float(critic) < 8:
            ccolor = "mix"
        else:
            ccolor = "good"
        user = soup.find(class_="user").text
        if float(user) < 5:
            ucolor = "bad"
        elif float(user) < 8:
            ucolor = "mix"
        else:
            ucolor = "good"
    except Exception:
        critic = "N/A"
        ccolor = "none"
        ucolor = "none"
        user = "N/A"

    # Returns scores
    return(critic, ccolor, user, ucolor)
