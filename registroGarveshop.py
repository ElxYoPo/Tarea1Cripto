from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random

#Func que añade digito verificador
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

# Generación de rut válido
r = int(round(2e7 * random.random()) + 5e6)
v = digito_verificador(r)
r = str(r) + "-" + str(v)

PATH = "C:\Program Files (x86)\msedgedriver.exe"
driver = webdriver.Edge(PATH)

driver.get("https://www.garveshop.com")
print(driver.title)
time.sleep(3)
driver.find_element_by_id("btn-cerrar").click()
driver.find_element_by_id("pull").click()
time.sleep(1)
register = driver.find_element_by_link_text("CASILLA GRATIS")
time.sleep(1)
print(register)
register.click()
print(driver.title)
time.sleep(1)
driver.find_element_by_id("nombre").send_keys("Benito")
driver.find_element_by_id("apellido_p").send_keys("Ben")
driver.find_element_by_id("rut").send_keys(r)
# driver.find_element_by_id("email").send_keys(r+"@benito.cum")
# driver.find_element_by_id("reemail").send_keys(r+"@benito.cum")
driver.find_element_by_id("email").send_keys("xoyey61513@dwgtcm.com")
driver.find_element_by_id("reemail").send_keys("xoyey61513@dwgtcm.com")
driver.find_element_by_id("telefono").send_keys("Benito")
Select(driver.find_element_by_id("region")).select_by_value('1')
driver.find_element_by_id("direccion").send_keys("Avenida siempre viva jaja simpsons")
driver.find_element_by_id("pass").send_keys("Benny"+r)
driver.find_element_by_id("pass2").send_keys("Benny"+r)
driver.find_element_by_id("terminos").click()
time.sleep(3)
driver.find_element_by_id("registrar").click()
time.sleep(10)

driver.close()