from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('./chromedriver.exe')
driver.get("https://www.google.com")
assert "Google" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("selenium install ubuntu python")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
link = driver.find_element_by_partial_link_text('pypi.org').click()
elem = driver.find_element_by_name("q")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
driver.find_elements_by_partial_link_text("selenium")[1].click()
driver.close()
