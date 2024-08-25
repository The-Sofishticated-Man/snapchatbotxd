from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Victim:
    def __init__(self, victimElement: WebElement, driver: WebDriver) -> None:
        self.element = victimElement
        self.context = driver
        self._name = self.element.find_element(By.CSS_SELECTOR, "span .nonIntl").text
        self._isSelected = False

    @property
    def name(self):
        self._name = self.element.find_element(By.CSS_SELECTOR, "span .nonIntl").text
        return self._name

    @property
    def isSelected(self):
        return self._isSelected

    def select(self):
        if not self._isSelected:
            self.element.click()
            self._isSelected = True

    def unselect(self):
        if self._isSelected:
            try:
                victimBar = self.context.find_element(By.CLASS_NAME, "k1IaM")
                closeBtn = victimBar.find_element(By.CLASS_NAME, "kY4Ky BWtqT")
            except NoSuchElementException:
                self._isSelected = False
            else:
                closeBtn.click()
                self._isSelected = False
    def sendMessage(self, message: str):
        if not self.isSelected:
            self.select()
        messageBar = self.context.find_element(By.CSS_SELECTOR, "div[role='textbox']")
        messageBar.click()
        messageBar.send_keys(message + Keys.ENTER)