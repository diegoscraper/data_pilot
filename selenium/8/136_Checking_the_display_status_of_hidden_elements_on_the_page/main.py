from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

if driver.find_element(By.ID, "hbutton").is_displayed():
    print('displayed')
print('not displayed')

# time.sleep(5)

driver.quit()
