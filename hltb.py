import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup as bs


# Gets game info from HowLongToBeat.com
def hltb_info(name):
    # Prevents chrome window from displaying
    options = Options()
    options.add_argument("headless")
    options.add_argument("disable-gpu")
    options.add_argument("no-sandbox")

    # Setting variables for heroku deployment
    GOOGLE_CHROME_BIN = "/app/.apt/usr/bin/google-chrome"
    CHROMEDRIVER = "/app/.chromedriver/bin/chromedriver"
    options.binary_location = GOOGLE_CHROME_BIN

    # Initializes Chrome Driver
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER, options=options)

    # Sets base url for HowLongToBeat
    hltb = "https://howlongtobeat.com/#search"
    driver.get(hltb)
    searchBox = driver.find_element_by_class_name("global_search_box")
    searchBox.send_keys(name)

    # Waits 2 seconds for the webpage to load
    time.sleep(2)

    # Finds the elements that we're looking for
    elements = driver.find_elements_by_xpath("//li/div/h3/a")

    # Gets text and url values from element objects
    games = []
    for e in elements:
        games.append({
                        "name": e.text,
                        "length": "N/A",
                        "url": e.get_attribute("href"),
                        "release": "N/A",
                        "critic": "N/A",
                        "ccolor": "none",
                        "user": "N/A",
                        "ucolor": "none",
                        "platforms": ["N/A"],
                        "genre": ["N/A"],
                        "img": "N/A"
        })

    # Ends web driver
    driver.quit()

    # Gets length of each game
    for game in games:
        game["length"], game["img"] = get_length(game["url"])

    # Return list of games
    return games


def get_length(url):

    # User Agent needed to access the site
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
               " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88"
               " Safari/537.36"}

    # Load the page
    r = requests.get(url, headers=headers)
    # Convert to a beautiful soup object
    soup = bs(r.content, "html5lib")

    elements = soup.find_all(class_="short")

    # Get the right completion time
    length = "--"
    for e in elements:
        if e.find("h5").text == "Main Story":
            length = e.find("div").text
        if e.find("h5").text == "Main + Extras":
            if e.find("div").text != "-- ":
                length = e.find("div").text

    # Also get game artwork
    # Using try to prevent errors if the image does not exist
    try:
        img = soup.find(class_="game_image").img["src"]
    except Exception:
        img = ""

    return(length, img)
