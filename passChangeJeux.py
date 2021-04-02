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
time.sleep(1)
driver.find_element_by_id("logged-user-avatar").click()
driver.find_element_by_class_name("icon--settings").click()
time.sleep(1)
driver.find_element_by_id("profile-settings-change-password").click()
driver.find_element_by_id("profile-settings-old-password").send_keys("aaaaaa")
driver.find_element_by_id("profile-settings-new-password").send_keys("aaaaaa")
driver.find_element_by_id("profile-settings-new-password2").send_keys("aaaaaa")
driver.find_element_by_id("profile-settings-new-password-submit").click()
time.sleep(10)



driver.close()