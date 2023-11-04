from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options)

URL = "https://books.toscrape.com/"
driver.get(URL)

#
# divx = driver.find_elements(By.TAG_NAME, "div")
#
# for i, div in enumerate(divx):
#     # print(i, "-->", div.text)
#     match i:
#         case 3:
#             uls = div.find_elements(By.TAG_NAME, "ul")
#
#             az = div.find_elements(By.TAG_NAME, "a")
#             for f, g in enumerate(az):
#                 print(f, "-->>", g.text)


sectionz = driver.find_elements(By.TAG_NAME, "section")
for idx, section in enumerate(sectionz):
    lizes = section.find_elements(By.TAG_NAME, "li")
    for l, li in enumerate(lizes):
        print(l, li.text)
