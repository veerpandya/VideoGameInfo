import requests
from bs4 import BeautifulSoup as bs


# Get release date info from google
def get_release(name):
    # Replaces spaces with + to be used in the url
    name = name.replace(" ", "+")

    # User Agent needed to access the site
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
               " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88"
               " Safari/537.36"}

    baseURL = "https://www.google.com/search?q="

    # Makes new url for the game
    gameURL = baseURL + name + "+release+date"

    # Load the webpage content
    r = requests.get(gameURL, headers=headers)

    # Convert to a beautiful soup object
    soup = bs(r.content, "lxml")

    # Find release date
    # Using try to cover cases where it's not found
    try:
        release_date = soup.find(class_="Z0LcW XcVN5d").text
    except Exception:
        release_date = "N/A"

    return(release_date)
