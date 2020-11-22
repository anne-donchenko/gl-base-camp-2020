from selenium.webdriver.common.by import By

class Config() :

    URL = 'https://www.globallogic.com/ua/careers/'
    SEARCH_URL = 'https://www.globallogic.com/ua/career-search-page/'
    SEARCH_FIELD = (By.ID, 'by_keyword')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="hero"]/div/div/div/div/div/div/div/form/div/button')
    COOKIE_ALLOW_ALL_BUTTON = (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
    FIND_BY_FIRST = (By.CSS_SELECTOR, 'p.mb-0')
    SEARCH_FIELD_IS_MISSING = "Search field is missing"
   
    def __init__(self) :
        super().__init__()