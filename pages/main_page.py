from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element_by_css_selector("#login_link")
        login_link.click()
    #By.CSS_SELECTOR, "#login_link_invalid"
    def should_be_login_link(self): 
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is absent on the page"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    