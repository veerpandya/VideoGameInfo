import requests
from bs4 import BeautifulSoup as bs


# Get game info from wikipedia.com
def wiki_info(name):
    # Replaces spaces with _ to be used in the url
    name = name.replace(" ", "_")

    # User Agent needed to access the site
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
               " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88"
               " Safari/537.36"}

    baseURL = "https://en.wikipedia.org/wiki/"

    # Makes new url for the game
    gameURL = baseURL + name

    # Load the webpage content
    r = requests.get(gameURL, headers=headers)

    # Convert to a beautiful soup object
    soup = bs(r.content, "html5lib")

    # Gets the infobox from the page
    infobox = soup.find("table", class_="infobox")

    # If wiki page doesn't exist, skip
    if infobox is not None:
        # Using try to avoid errors
        try:
            # Gets game's platform data from the box
            platform_data = infobox.find("th", text="Platform(s)").parent

            # Gets platform info
            platform_info = platform_data.select("td a")

            # Converts platform info into text
            platforms = get_text(platform_info)

            # Same steps for genre info
            genre_data = infobox.find("th", text="Genre(s)").parent
            genre_info = genre_data.select("td a")
            genre = get_text(genre_info)

        except Exception:
            platforms = ["N/A"]
            genre = ["N/A"]

    else:
        platforms = ["N/A"]
        genre = ["N/A"]

    # Returns info
    return(platforms, genre)


# Converts list of elements into list of text
def get_text(elements):
    text_list = []
    for element in elements:
        text = element.text
        if text[0] != "[":
            text_list.append(text)

    return text_list
