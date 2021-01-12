import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# Gets game info from HowLongToBeat.com
def hltb_info(name):
    # Prevents chrome window from displaying
    options = Options()
    options.add_argument("headless")

    # Initializes Chrome Driver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # Sets base url for HowLongToBeat
    hltb = "https://howlongtobeat.com/#search"
    driver.get(hltb)
    searchBox = driver.find_element_by_class_name("global_search_box")
    searchBox.send_keys(name)

    # Waits 2 seconds for the webpage to load
    time.sleep(2)

    # Finds the elements that we're looking for
    games = driver.find_elements_by_xpath("//li/div/h3/a")

    # Gets text value from element objects
    titles = []
    for e in games:
        titles.append(e.text)

    # Ends web driver
    driver.quit()

    # Return list of games
    return(titles)
