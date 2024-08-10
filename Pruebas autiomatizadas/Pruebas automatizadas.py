import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import HtmlTestRunner

class MaxLoginTest(unittest.TestCase):

    def setUp(self):
        # Especifica la ruta correcta al archivo `chromedriver.exe`
        self.driver = webdriver.Chrome(executable_path="C:/Users/letic/Downloads/chromedriver-win32/chromedriver.exe")
        self.driver.maximize_window()

    def test_login_max(self):
        driver = self.driver
        driver.get("https://auth.max.com/login?_referrer=eyJlbGVtZW50IjoiQnV0dG9uIiwic2NyZWVuTmFtZSI6IlZlciBwZWxjdWxhcyB5IHNlcmllcyBvbmxpbmUgfCBNYXggIiwic2NyZWVuVVJJIjoiaHR0cHM6Ly93d3cubWF4LmNvbS9kby9lcyIsImxvY2F0aW9uIjoiSG9tZXBhZ2UvVmVyIHBlbGN1bGFzIHkgc2VyaWVzIG9ubGluZSB8IE1heCB8YmFuZHwxMjY5NTQiLCJsb2NhdGlvblBvc2l0aW9uIjowLCJ0YXJnZXRUZXh0IjoiSW5ncmVzYSJ9")

        time.sleep(3)  # Esperar a que la página cargue

        # Localizar el campo de nombre de usuario
        username_field = driver.find_element(By.ID, "login-username-input")
        username_field.clear()
        username_field.send_keys("leticia02@outlook.es")

        # Localizar el campo de contraseña
        password_field = driver.find_element(By.ID, "login-password-input")
        password_field.clear()
        password_field.send_keys("Dorcadela17")

        # Simular el envío del formulario
        password_field.send_keys(Keys.RETURN)

        time.sleep(5)  # Esperar a que el siguiente paso cargue

        # Verificar si el inicio de sesión fue exitoso
        self.assertIn("Página Principal", driver.title, "El inicio de sesión falló")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reportes"))


