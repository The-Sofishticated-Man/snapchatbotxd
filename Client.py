from Victim import Victim

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class Client:
    def __init__(self) -> None:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 15)

    def login(self, username: str, password: str):
        self.driver.get("https://snapchat.com/")

        # wait for username field to appear, find username field and enter username
        self.wait.until(EC.element_to_be_clickable((By.ID, "ai_input"))).send_keys(
            username + Keys.ENTER
        )

        # wait until password field appears, find password field and enter password
        self.wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        ).send_keys(password + Keys.ENTER)

        while True:
            # check if there is an error pop up and refresh if there is
            try:
                errorPopUp = self.driver.find_element(By.CLASS_NAME, "O1Map")
            except NoSuchElementException:
                pass
            else:
                self.driver.refresh()

            # check if there is a notification pop up signifying successful login and close it and exit the loop
            try:
                closeButton = self.driver.find_element(By.CLASS_NAME, "cV8g1")
            except NoSuchElementException:
                pass
            else:
                closeButton.click()
                break
        print("successfully logged in")

    def loadVictims(self):
        while True:
            try:
                victimElements = self.wait.until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "O4POs"))
                )
            except TimeoutError:
                self.driver.refresh()
            else:
                self.victims = [
                    Victim(victimElement, self.driver)
                    for victimElement in victimElements
                ]
                return self.victims
