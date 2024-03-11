# webdriver_setup.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from config import get_chrome_options

def setup_webdriver():
    chrome_options = get_chrome_options()
    chrome_driver_path = 'd:\chromedriver-win64\chromedriver.exe'
    service = ChromeService(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
