from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config

class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.config = Config()

class GLCareersResultPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @property
    def AllowCookieButton(self):
        return self.browser.find_element(*self.config.COOKIE_ALLOW_ALL_BUTTON)

    def open(self, by_keyword=None):
        self.browser.implicitly_wait(10)
        self.browser.get(f'{self.config.SEARCH_URL}?keywords={by_keyword}&experience=&locations=&c=')
        self.AllowCookieButton.click()
        return True

    def findFirst(self):
        return self.browser.find_element(*self.config.FIND_BY_FIRST).text

    def check_firstResult_exists(self):
        _field = self.findFirst
        print(_field)
        return _field is not None
        


class BaseApp(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @property
    def AllowCookieButton(self):
        return self.browser.find_element(*self.config.COOKIE_ALLOW_ALL_BUTTON)

    @property
    def search_field(self):
        return self.browser.find_element(*self.config.SEARCH_FIELD)
        
    @property
    def search_button(self):
        return self.browser.find_element(self.config.SEARCH_BUTTON)

    def open(self):
        self.browser.implicitly_wait(10)
        self.browser.get(self.config.URL)
        self.AllowCookieButton.click()

    def search_vacancy(self, vacancy, enter=False):
        self.search_field.send_keys(vacancy)
        if enter:
            self.search_field.send_keys(Keys.RETURN)
        else:
            self.search_button.click()

        return True

    def check_field_exists(self):
        _field = self.search_field

        return _field is not None


# start the browser
driver = webdriver.Chrome('../../chromedriver.exe')

def test_search_field_exist():
    careersPage = BaseApp(driver)
    careersPage.open()

    assert careersPage.check_field_exists(), self.config.SEARCH_FIELD_IS_MISSING



def test_it_can_search():
    careersPage = BaseApp(driver)
    careersPage.open()
    careersPage.search_vacancy('QA')

    assert careersPage.check_field_exists(), self.config.SEARCH_FIELD_IS_MISSING
    

def test_it_can_open_results_page():
    resultPage = GLCareersResultPage(driver)
    assert resultPage.open(by_keyword='')
    assert resultPage.check_firstResult_exists()

test_it_can_open_results_page()