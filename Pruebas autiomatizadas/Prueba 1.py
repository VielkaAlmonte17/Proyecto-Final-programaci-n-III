from selenium import webdriver

# Inicializa el WebDriver
driver = webdriver.Chrome()

# Imprime la versión de ChromeDriver
print(driver.capabilities['chrome']['chromedriverVersion'])

# Cierra el WebDriver
driver.quit()
