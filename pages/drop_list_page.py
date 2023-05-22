import time

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from locators import locators
from pages.base_page import BasePage


class DropListPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def click_panel(self, element_panel_locator):
        self.click(element_panel_locator)

    def panel_text(self, element_panel_text_locator):
        return self.getting_text(element_panel_text_locator)

    def waiting_for_panel(self, element_panel_locator):
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(element_panel_locator))

    def drop_panels(self, element_panel_locator, element_panel_text_locator):
        self.waiting_for_panel(element_panel_locator)
        self.click_panel(element_panel_locator)
        return self.panel_text(element_panel_text_locator)



