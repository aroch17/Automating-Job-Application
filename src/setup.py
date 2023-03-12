from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os

options = Options()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'

chrome_driver_path = os.environ.get("CHROME_DRIVER_PATH")

driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)

actions = ActionChains(driver)
