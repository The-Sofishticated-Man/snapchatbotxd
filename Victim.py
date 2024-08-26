import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Victim:
    selectedInstance = None
    def __init__(self, victimElement: WebElement, driver: WebDriver) -> None:
        self.element = victimElement
        self.context = driver
    
    @property
    def name(self):
        return self.element.find_element(By.CSS_SELECTOR, "span .nonIntl").text

    @property
    def isSelected(self):
        return self == Victim.selectedInstance 

    def select(self):
        if not self.isSelected:
            self.element.click()
            Victim.selectedInstance = self

    def unselect(self):
        if self.isSelected:
            victimBar = self.context.find_element(By.CLASS_NAME, "k1IaM")
            closeBtn = victimBar.find_element(By.CLASS_NAME, "kY4Ky BWtqT")
            closeBtn.click()
            Victim.selectedInstance = None

    def sendMessage(self, message: str):
        time.sleep(0.5)
        if not self.isSelected:
            self.select()
        messageBar = self.context.find_element(By.CSS_SELECTOR, "div[role='textbox']")
        messageBar.click()
        messageBar.send_keys(message + Keys.ENTER)
