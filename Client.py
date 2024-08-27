from Victim import Victim

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class Client:
    def __init__(self) -> None:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self, username: str, password: str):
        self.driver.get("https://snapchat.com/")

        # find username field and enter username
        usernameInput = self.driver.find_element(By.ID, "ai_input")
        usernameInput.send_keys(username + Keys.ENTER)
        time.sleep(5)

        # find password field and enter password
        passwordInput = self.driver.find_element(By.NAME, "password")
        passwordInput.send_keys(password + Keys.ENTER)
        while True:
            # check if there is an error pop up and refresh if there is
            try:
                errorPopUp = self.driver.find_element(By.CLASS_NAME, "O1Map")
            except NoSuchElementException:
                pass
            else:
                self.driver.refresh()

            # check if there is a notification pop up signifying successful login and close it if there is
            try:
                closeButton = self.driver.find_element(By.CLASS_NAME, "cV8g1")
            except NoSuchElementException:
                pass
            else:
                closeButton.click()
                break

    def loadVictims(self):
        time.sleep(3)
        while True:
            try:
                victimElements = self.driver.find_elements(By.CLASS_NAME, "O4POs")
            except NoSuchElementException:
                time.sleep(0.5)
                print("couldn't find victims")
            else:
                print(f"found {len(victimElements)} victims")
                self.victims = [
                    Victim(victimElement, self.driver)
                    for victimElement in victimElements
                ]
                return self.victims
