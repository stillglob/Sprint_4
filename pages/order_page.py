import selenium
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import random
from locators import locators
from pages.base_page import BasePage

class OrderPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        return self.send_keys(locators.OrderPageAuthLocators.NAME_FIELD, name)

    def set_last_name(self, last_name):
        self.send_keys(locators.OrderPageAuthLocators.LAST_NAME_FIELD, last_name)

    def set_address(self, u_address):
        self.send_keys(locators.OrderPageAuthLocators.ADDRESS_FIELD, u_address)

    def set_station(self, u_station):
        self.click(locators.OrderPageAuthLocators.STATION_FIELD)
        self.send_keys(locators.OrderPageAuthLocators.STATION_FIELD, u_station)
        self.click(locators.OrderPageAuthLocators.STATION_MENU)

    def set_telephone(self, u_telephone):
        self.click(locators.OrderPageAuthLocators.TELEPHONE_FIELD)
        self.send_keys(locators.OrderPageAuthLocators.TELEPHONE_FIELD, u_telephone)

    def next_button_click(self):
        self.click(locators.OrderPageAuthLocators.NEXT_BTN)

    def order_upper_button_click(self):
        self.click(locators.HomePageLocators.ORDER_BTN_UPPER)

    def order_lower_button_click(self):
        self.click(locators.HomePageLocators.ORDER_BTN_LOWER)

    def set_date(self, r_date):
        self.click(locators.OrderPageAuthLocators.DATE_FIELD)
        self.send_keys(locators.OrderPageAuthLocators.DATE_FIELD, r_date)
        self.send_enter(locators.OrderPageAuthLocators.DATE_FIELD)

    def set_rent(self):
        self.click(locators.OrderPageAuthLocators.RENT_PERIOD_FIELD)
        self.click(locators.OrderPageAuthLocators.RENT_PERIOD_MENU)

    def set_color(self):
        if random.random() == 0:
            self.click(locators.OrderPageAuthLocators.COLOR_SELECT_BLACK)
        else:
            self.click(locators.OrderPageAuthLocators.COLOR_SELECT_GREY)

    def send_comment(self, random_comment):
        self.click(locators.OrderPageAuthLocators.COMMENT_FIELD)
        self.send_keys(locators.OrderPageAuthLocators.COMMENT_FIELD, random_comment)

    def order_btn2_click(self):
        self.click(locators.OrderPageAuthLocators.ORDER_BTN2)

    def success_order_bar_check(self):
        self.click(locators.OrderPageAuthLocators.SUCCESS_ORDER_CHECK)
        return self.getting_text(locators.OrderPageAuthLocators.SUCCESS_ORDER_CHECK)

    def confirm_order_click(self):
        self.click(locators.OrderPageAuthLocators.CONFIRM_ORDER_BTN)

    def status_btn_click(self):
        self.click(locators.OrderPageAuthLocators.STATUS_BTN)

    def yandex_logo_click(self):
        self.click(locators.OrderPageAuthLocators.YANDEX_LOGO)

    def scooter_logo_click(self):
        self.click(locators.OrderPageAuthLocators.SCOOTER_LOGO)

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_for_load_page(self):
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(locators.YandexPageLocators.DZEN_LOGO))

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(locators.HomePageLocators.ORDER_BTN_UPPER))

    def check_yandex_log_in_btn(self):
        return self.getting_text(locators.YandexPageLocators.YANDEX_LOG_IN_BTN)

    def check_scooter_page(self):
        return self.getting_text(locators.HomePageLocators.SCOOTER_HOME_HEADER)

    def make_order(self, name, last_name, u_address, u_station, u_telephone, r_date, random_comment):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(u_address)
        self.set_station(u_station)
        self.set_telephone(u_telephone)
        self.next_button_click()
        self.set_date(r_date)
        self.set_rent()
        self.set_color()
        self.send_comment(random_comment)
        self.order_btn2_click()
        self.confirm_order_click()

    def make_order_upper_btn_success_order(self, name, last_name, u_address, u_station, u_telephone, r_date, random_comment):
        self.order_upper_button_click()
        self.make_order(name, last_name, u_address, u_station, u_telephone, r_date, random_comment)
        return self.success_order_bar_check()

    def make_order_lower_btn_success_order(self, name, last_name, u_address, u_station, u_telephone, r_date, random_comment):
        self.order_lower_button_click()
        self.make_order(name, last_name, u_address, u_station, u_telephone, r_date, random_comment)
        return self.success_order_bar_check()

    def yandex_logo_click_with_upper_btn_order(self, name, last_name, u_address, u_station, u_telephone, r_date, random_comment):
        self.order_upper_button_click()
        self.make_order(name, last_name, u_address, u_station, u_telephone, r_date, random_comment)
        self.status_btn_click()
        self.yandex_logo_click()
        self.switch_to_new_window()
        self.wait_for_load_page()
        return self.check_yandex_log_in_btn()

    def yandex_logo_click_with_lower_btn_order(self, name, last_name, u_address, u_station, u_telephone, r_date, random_comment):
        self.make_order_lower_btn_success_order(name, last_name, u_address, u_station, u_telephone, r_date, random_comment)
        self.status_btn_click()
        self.yandex_logo_click()
        self.switch_to_new_window()
        self.wait_for_load_page()
        return self.check_yandex_log_in_btn()

    def scooter_logo_click_with_upper_btn_order(self, name, last_name, u_address, u_station, u_telephone, r_date, random_comment):
        self.make_order_upper_btn_success_order(name, last_name, u_address, u_station, u_telephone, r_date, random_comment)
        self.status_btn_click()
        self.scooter_logo_click()
        self.wait_for_load_home_page()
        return self.check_scooter_page()

    def scooter_logo_click_with_lower_btn_order(self, name, last_name, u_address, u_station, u_telephone, r_date, random_comment):
        self.make_order_lower_btn_success_order(name, last_name, u_address, u_station, u_telephone, r_date, random_comment)
        self.status_btn_click()
        self.scooter_logo_click()
        self.wait_for_load_home_page()
        return self.check_scooter_page()








