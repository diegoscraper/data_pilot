import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")

# * QUALQUER UM DOS DOIS ABAIXO DÃO CERTO:
driver = webdriver.Chrome(options)
# driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.get("http://tutorialsninja.com/demo/")

page_title = driver.title
print(page_title)

driver.quit()
