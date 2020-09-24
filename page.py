from element import get_element, click_bar
from locators import PageLocators

import data

class BasePage:
    def __init__(self, driver):
        self.driver = driver

class HTTP_org_page(BasePage):

    def get_logo_text(self):
        return get_element(self.driver, PageLocators.logo_text).text

    def click_Http_methods_bar(self):
        click_bar(self.driver, PageLocators.HTTP_Methods_bar).click()

    def click_Http_delete_bar(self):
        click_bar(self.driver, PageLocators.HTTP_Methods_DELETE_bar).click()

    def click_HTTP_delete_TRYitOUT_button(self):
        click_bar(self.driver, PageLocators.HTTP_Methods_DELETE_TRYitOUT_button).click()
