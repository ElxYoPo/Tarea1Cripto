from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\msedgedriver.exe"
driver = webdriver.Edge(PATH)

driver.get("https://www.jeux.fr/")
driver.maximize_window()
print(driver.title)
time.sleep(2)
driver.find_element_by_id("onetrust-accept-btn-handler").click()
time.sleep(1)
driver.find_element_by_id("login-button-nav").click()
time.sleep(1)
driver.find_element_by_id("popup-login-username").send_keys("pabliteclavite123")
driver.find_element_by_id("popup-login-password").send_keys("aaaaaa")
driver.find_element_by_id("popup-login-button").click()
time.sleep(10)



driver.close()