import pytest
from selenium import webdriver
from locators import locators
from urls import scooter_home_page

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(scooter_home_page)
    driver.find_element(*locators.HomePageLocators.COOKIE_ACC_BNT).click()
    yield driver
    driver.quit()





