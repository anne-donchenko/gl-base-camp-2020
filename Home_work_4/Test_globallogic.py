from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('./chromedriver.exe')
driver.get("https://www.globallogic.com/ua/careers/")
assert "GlobalLogic" in driver.title
elem = driver.find_element_by_name("keywords")
elem.send_keys("QA")
elem.send_keys(Keys.RETURN)
assert "QA" in driver.page_source
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.mb-0")))
content = driver.find_element_by_css_selector("p.mb-0").text
print(content)
driver.close()