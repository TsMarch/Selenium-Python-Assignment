from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://ya.ru/"

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = URL

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator))

    def go_to_site(self):
        return self.driver.get(self.base_url)
    
    def switch_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])
    
    def get_current_url(self) -> str:
        return self.driver.current_url

