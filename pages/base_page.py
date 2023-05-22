from selenium.webdriver import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        self.driver.find_element(*element).click()

    def find(self, element):
        self.driver.find_element(*element)

    def attribute(self, element):
        self.driver.find_element(*element).get_tag('')

    def send_keys(self, element, string):
        self.driver.find_element(*element).send_keys(string)

    def send_enter(self, element):
        self.driver.find_element(*element).send_keys(Keys.ENTER)

    def getting_text(self, element):
        return self.driver.find_element(*element).text




