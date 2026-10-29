from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login2")