from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random

#Copypaste del código usado para generar rut en garveshop 2
def digito_verificador(rut):
    producto = [2,3,4,5,6,7] # producto de con el cual se debe multiplicar
    list_rut = list(map(int, str(rut))) # convertir en lista el rut
    list_rut.reverse() # revertir los valores
    contador = 0
    pivote = 0
    for i in list_rut:
        if pivote >= len(producto): # si el pivote pasa la cantidad del largo de producto, se debe reiniciar
            pivote = 0
        contador = contador+(i*producto[pivote])
        pivote += 1
    suma_dig = 11-(contador%11) # obtener el resto menos 11 de la suma
    # definir digito verificador
    if suma_dig == 11:
        verificador = 0
    elif suma_dig == 10:
        verificador = 'K'
    else:
        verificador = suma_dig

    return verificador

#Copypaste del código usado para generar rut en garveshop 1
r = int(round(2e7 * random.random()) + 5e6)
v = digito_verificador(r)
r = str(r) + "-" + str(v)

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
driver.find_element_by_id("popup-login-register").click()
time.sleep(1)
Select(driver.find_element_by_id("popup-register-dob-month")).select_by_value('6')
Select(driver.find_element_by_id("popup-register-dob-day")).select_by_value('25')
Select(driver.find_element_by_id("popup-register-dob-year")).select_by_value('1997')
time.sleep(1)
driver.find_element_by_id("popup-register-username").send_keys(r)
driver.find_element_by_id("popup-register-email").send_keys(r+"@arayajaquercito.com")
driver.find_element_by_id("popup-register-password").send_keys(r)
time.sleep(1)
driver.find_element_by_id("popup-register-button").click()
time.sleep(10)

driver.close()