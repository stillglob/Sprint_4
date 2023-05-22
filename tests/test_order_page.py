from unittest import result
import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import locators
from selenium import webdriver
from pages.order_page import OrderPage
from person import dat_list

class TestOrderPage:

    @allure.title('заказ через верхнюю кнопку, всплывающее окно с сообщением об успешном создании заказа')
    @pytest.mark.parametrize('name, last_name, u_address, u_station, u_telephone, r_date, random_comment', dat_list)
    def test_upper_order_btn_success_order(self, driver, name, last_name, u_address, u_station, u_telephone, r_date, random_comment):
        order_page = OrderPage(driver)
        order_page.make_order_upper_btn_success_order(name, last_name, u_address, u_station, u_telephone, r_date, random_comment)
        assert 'Заказ оформлен' in order_page.success_order_bar_check()

    @allure.title('заказ через нижнюю кнопку, всплывающее окно с сообщением об успешном создании заказа')
    @pytest.mark.parametrize('name, last_name, u_address, u_station, u_telephone, r_date, random_comment', dat_list)
    def test_lower_order_btn_success_order(self, driver, name, last_name, u_address, u_station, u_telephone, r_date, random_comment):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        order_page = OrderPage(driver)
        order_page.make_order_lower_btn_success_order(name, last_name, u_address, u_station, u_telephone, r_date, random_comment)
        assert 'Заказ оформлен' in order_page.success_order_bar_check()

    @allure.title('заказ через верхнюю кнопку, клик на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    @pytest.mark.parametrize('name, last_name, u_address, u_station, u_telephone, r_date, random_comment', dat_list)
    def test_scooter_logo_click_with_upper_btn_order(self, driver, name, last_name, u_address, u_station, u_telephone, r_date, random_comment):
        order_page = OrderPage(driver)
        order_page.scooter_logo_click_with_upper_btn_order(name, last_name, u_address, u_station, u_telephone, r_date, random_comment)
        assert 'Самокат' in order_page.check_scooter_page()

    @allure.title('заказ через нижнюю кнопку, клик на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    @pytest.mark.parametrize('name, last_name, u_address, u_station, u_telephone, r_date, random_comment', dat_list)
    def test_scooter_logo_click_with_lower_btn_order(self, driver, name, last_name, u_address, u_station, u_telephone, r_date, random_comment):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        order_page = OrderPage(driver)
        order_page.scooter_logo_click_with_lower_btn_order(name, last_name, u_address, u_station, u_telephone, r_date, random_comment)
        assert 'Самокат' in order_page.check_scooter_page()

    @allure.title('заказ через верхнюю кнопку, клик на логотип Яндекса, в новом окне откроется главная страница Яндекса.')
    @pytest.mark.parametrize('name, last_name, u_address, u_station, u_telephone, r_date, random_comment', dat_list)
    def test_yandex_logo_click_with_upper_btn_order(self, driver, name, last_name, u_address, u_station, u_telephone, r_date, random_comment):
        order_page = OrderPage(driver)
        order_page.yandex_logo_click_with_upper_btn_order(name, last_name, u_address, u_station, u_telephone, r_date, random_comment)
        assert 'Войти' in order_page.check_yandex_log_in_btn()

    @allure.title('заказ через нижнюю кнопку, клик на логотип Яндекса, в новом окне откроется главная страница Яндекса.')
    @pytest.mark.parametrize('name, last_name, u_address, u_station, u_telephone, r_date, random_comment', dat_list)
    def test_yandex_logo_click_with_lower_btn_order(self, driver, name, last_name, u_address, u_station, u_telephone, r_date, random_comment):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        order_page = OrderPage(driver)
        order_page.yandex_logo_click_with_lower_btn_order(name, last_name, u_address, u_station, u_telephone, r_date, random_comment)
        assert 'Войти' in order_page.check_yandex_log_in_btn()

