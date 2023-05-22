import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import locators
from selenium import webdriver
import time
from pages.drop_list_page import DropListPage
from person import panels_text

class TestPanelsPage:

    @allure.title('выпадающий список в разделе «Вопросы о важном». совпадение текста с нажатой плашкой')
    @pytest.mark.parametrize('panel, panel_text, result', panels_text)
    def test_drop_panels_text_matches(self, driver, panel, panel_text, result):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        home_page = DropListPage(driver)
        panel_method, panel_locator = locators.DropListPageLocators.DROP_PANEL
        panel_locator = panel_locator.format(panel)
        element_panel_locator = panel_method, panel_locator
        panel_text_method, panel_text_locator = locators.DropListPageLocators.DROP_PANEL_TEXT
        panel_text_locator = panel_text_locator.format(panel_text)
        element_panel_text_locator = panel_text_method, panel_text_locator
        assert home_page.drop_panels(element_panel_locator, element_panel_text_locator) == result
