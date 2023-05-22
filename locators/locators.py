from selenium.webdriver.common.by import By

class HomePageLocators:
    ORDER_BTN_UPPER = [By.XPATH, "//button[1]"]
    ORDER_BTN_LOWER = [By.XPATH, "//div[5]/button"]
    COOKIE_ACC_BNT = [By.XPATH, "//button[@id='rcc-confirm-button']"]
    SCOOTER_HOME_HEADER = [By.CSS_SELECTOR, ".Home_Header__iJKdX"]


class OrderPageAuthLocators:
    NAME_FIELD = [By.XPATH, "//div[2]/div[1]/input"]
    LAST_NAME_FIELD = [By.XPATH, "//div[2]/div[2]/input"]
    ADDRESS_FIELD = [By.XPATH, "//div[2]/div[3]/input"]
    STATION_FIELD = [By.XPATH, "//div[1]/div[1]/input"]
    STATION_MENU = [By.XPATH, "//div[2]/div[4]/div/div[2]"]
    TELEPHONE_FIELD = [By.XPATH, "//div[2]/div[5]/input"]
    DATE_FIELD = [By.XPATH, "//div[1]/div[1]/div/input"]
    RENT_PERIOD_FIELD = [By.XPATH, '//div[2]/div[2]/div[2]/div']
    RENT_PERIOD_MENU = [By.XPATH, "//div[2]/div[2]/div[2]/div[2]"]
    COLOR_SELECT_BLACK = [By.XPATH, "//div[2]/div[2]/div[3]/label[1]"]
    COLOR_SELECT_GREY = [By.XPATH, "//div[2]/div[2]/div[3]/label[2]"]
    COMMENT_FIELD = [By.XPATH, "//div[2]/div[2]/div[4]/input"]
    STATUS_BTN = [By.XPATH, "//div[2]/div[5]/div[2]/button"]
    ORDER_BTN2 = [By.XPATH, '//div[2]/div[3]/button[2]']
    CONFIRM_ORDER_BTN = [By.XPATH, "//div[5]/div[2]/button[2]"]
    NEXT_BTN = [By.XPATH, "//div[2]/div[3]/button"]
    SCOOTER_LOGO = [By.XPATH, "//div[1]/div[1]/a[2]"]
    YANDEX_LOGO = [By.XPATH, "//div[1]/div[1]/a[1]"]
    SUCCESS_ORDER_CHECK = [By.XPATH, '//div[2]/div[5]/div[1]']

class DropListPageLocators:
    DROP_PANEL = [By.CSS_SELECTOR, '#accordion__heading-{}']
    DROP_PANEL_TEXT = [By.CSS_SELECTOR, '#accordion__panel-{}']

class YandexPageLocators:
    SEARCH_BTN = [By.XPATH, "//form/button"]
    DZEN_LOGO = [By.XPATH, "//header/div/div[1]/a"]
    YANDEX_LOG_IN_BTN = [By.XPATH, "//div[2]/div[3]/div/button"]
