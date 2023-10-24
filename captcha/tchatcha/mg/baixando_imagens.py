import time
from seleniumbase import Driver
from selenium import webdriver
from selenium.webdriver.common.by import By

# url = "https://www.sefaz.rs.gov.br/captchaweb/prCaptcha.aspx?f=getimage&rld=0&rdn=R1V8nv0TAHcI3flCpWi6cE3OKnQ2GabF"
url = "https://www.sei.mg.gov.br/sei/modulos/pesquisa/md_pesq_processo_pesquisar.php?acao_externa=protocolo_pesquisar&acao_origem_externa=protocolo_pesquisar&id_orgao_acesso_externo=0"

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

for i in range(5000):
    driver.get(url)
    driver.implicitly_wait(2)
    # img = driver.find_element(By.XPATH, "//body//img") # rs
    img = driver.find_element(By.XPATH, "//body//img")
    img.screenshot(f"{i}.png")

driver.quit()

# entra site
# baixa a imagem (100)
# salva na pasta com nome arquivo diferente
# entra site
