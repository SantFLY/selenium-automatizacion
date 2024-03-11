from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def click_reglas_alerta(driver, nombre_alerta):
    # Construye la expresión XPath para encontrar el elemento por href
    xpath_expression = '//a[@href="/main/alerts"]'

    # Espera hasta que el elemento sea clickeable
    reglas_alerta_element = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, xpath_expression)))
    reglas_alerta_element.click()


    nombre_alerta_locator = (By.CSS_SELECTOR, "[formcontrolname='name']")
    nombre_alerta_element = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable(nombre_alerta_locator))
    nombre_alerta_element.clear()
    nombre_alerta_element.send_keys(nombre_alerta)

    time.sleep(5)
    pr_locator = (By.CSS_SELECTOR, "[class='text-primary']")
    pr_element = WebDriverWait(driver, 10000).until(EC.element_to_be_clickable(pr_locator))
    pr_element.click()


    

    
