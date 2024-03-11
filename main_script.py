# main_script.py
from webdriver_setup import setup_webdriver
from login_actions import login
from actions_principal import click_reglas_alerta
import time
# Configurar el webdriver
driver = setup_webdriver()

# Realizar acciones de inicio de sesión
# Introducir las respectivas creedenciales Email , Password
login(driver, "practicanteti@grupoalto.com", "Polanco01031.")
# Introducir nombre de alerta a buscar
click_reglas_alerta(driver, "VIAJE EN DESTINO FINAL")


# Tiempo que el navegador estar abierto por segundos modificar segun se desee
time.sleep(1000)  

# Cerrar la ventana
driver.quit()
