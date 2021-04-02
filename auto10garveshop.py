from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\msedgedriver.exe"
driver = webdriver.Edge(PATH)

driver.get("https://garveshop.com/my_garve/usuario_registro/recuperar.php")
i = 0
time.sleep(2)
driver.find_element_by_id('cuenta').send_keys('19685')
while i<10:
    time.sleep(2)
    driver.find_element_by_id('restablecer').click()
    time.sleep(5)
    driver.back()
    i = i+1
driver.quit()