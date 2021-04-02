from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\msedgedriver.exe"
driver = webdriver.Edge(PATH)

driver.get("https://www.garveshop.com")
print(driver.title)
time.sleep(3)
driver.find_element_by_id("btn-cerrar").click()
driver.find_element_by_id("pull").click()
time.sleep(1)
driver.find_element_by_link_text("LOGIN").click()
time.sleep(1)
driver.find_element_by_link_text("Recuperar Contraseña").click()
time.sleep(1)
driver.find_element_by_id("numero_cliente").send_keys("19696")
time.sleep(10)

driver.close()