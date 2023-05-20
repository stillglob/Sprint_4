import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import locators
from selenium import webdriver
import time
from pages.drop_list_page import DropListPage

panels_text = [
        [0, 0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
        [1, 1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
        [2, 2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
        [3, 3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
        [4, 4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
        [5, 5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
        [6, 6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
        [7, 7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
    ]

class TestPanelsPage:

    @allure.title('выпадающий список в разделе «Вопросы о важном». совпадение текста с нажатой плашкой')
    @pytest.mark.parametrize('panel, panel_text, result', panels_text)
    def test_drop_panels_text_matches(self, driver, panel, panel_text, result):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.find_element(*locators.HomePageLocators.COOKIE_ACC_BNT).click()
        home_page = DropListPage(driver)
        panel_method, panel_locator = locators.DropListPageLocators.DROP_PANEL
        panel_locator = panel_locator.format(panel)
        element_panel_locator = panel_method, panel_locator
        panel_text_method, panel_text_locator = locators.DropListPageLocators.DROP_PANEL_TEXT
        panel_text_locator = panel_text_locator.format(panel_text)
        element_panel_text_locator = panel_text_method, panel_text_locator
        assert home_page.drop_panels(element_panel_locator, element_panel_text_locator) == result
        driver.quit()
