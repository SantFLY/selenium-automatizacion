# login_actions.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    driver.get("https://intransit-qa.altomovup.com/login")

    # Agregar el código para el inicio de sesión
    username_locator = (By.CSS_SELECTOR, "[formcontrolname='email']")
    username_element = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable(username_locator))
    username_element.clear()
    username_element.send_keys(username)

    password_locator = (By.CSS_SELECTOR, "[formcontrolname='password']")
    password_element = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable(password_locator))
    password_element.clear()
    password_element.send_keys(password)

    login_button_locator = (By.CSS_SELECTOR, "button.btn.btn-block.btn-primary.mb-2.fs-15")
    login_button_element = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable(login_button_locator))
    login_button_element.click()

    cuenta_demo_locator = (By.CSS_SELECTOR, "label.item-account.fs-13.c-pointer")
    cuenta_demo_element = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable(cuenta_demo_locator))
    cuenta_demo_element.click()

   
    
    


