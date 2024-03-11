# config.py

from selenium.webdriver.chrome.options import Options

def get_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    return chrome_options
