from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

driver.find_element(By.LINK_TEXT, "compendiumdev").click()

time.sleep(5)

driver.quit()
