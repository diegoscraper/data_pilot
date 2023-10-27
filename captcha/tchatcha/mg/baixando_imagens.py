import time
from seleniumbase import Driver
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.sei.mg.gov.br/sei/modulos/pesquisa/md_pesq_processo_pesquisar.php?acao_externa=protocolo_pesquisar&acao_origem_externa=protocolo_pesquisar&id_orgao_acesso_externo=0"
abs_path = "C:\\Users\\diego\\Desktop\\data_pilot\\captcha\\tchatcha\\mg\\bdcaptcha\\"

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

for i in range(1000):
    driver.get(url)
    driver.implicitly_wait(2)
    img = driver.find_element(By.XPATH, "//img[@id='imgCaptcha']")
    img.screenshot(f"{abs_path}{i}.png")

driver.quit()

