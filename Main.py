from Victim import Victim

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

USERNMAME = "hmaloney2024"
PASSWORD = "mal51159"

driver.get("https://snapchat.com/")
username = driver.find_element(By.ID, "ai_input")
username.send_keys(USERNMAME + Keys.ENTER)
time.sleep(5)
password = driver.find_element(By.NAME, "password")
password.send_keys(PASSWORD + Keys.ENTER)
try:
    errorPopUp = driver.find_element(By.CLASS_NAME, "O1Map")
    driver.refresh()
except NoSuchElementException:
    pass
time.sleep(10)

try:
    notificationPopUp = driver.find_element(By.CLASS_NAME, "gIloE")
    closeButton = driver.find_element(By.CLASS_NAME, "cV8g1")
    closeButton.click()
except NoSuchElementException:
    pass
time.sleep(4)


time.sleep(4)

victimElements = driver.find_elements(By.CLASS_NAME, "O4POs")
victims = [Victim(victimElement, driver) for victimElement in victimElements]

victims[0].sendMessage("hi there my name is hmaloney2024")
victims[1].sendMessage("hi there my name is john cena ")