from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")

element_location = driver.find_element(By.NAME, "search").location

print(element_location)

print(element_location.get("x"))

print(element_location.get("y"))


driver.quit()
