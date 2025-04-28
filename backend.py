import pandas
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def humanLikeTyping(element, text, delay=0.1):
    for character in text:
        element.send_keys(character)
        time.sleep(random.uniform(0.1, delay))

def processar(email, senha, excel_path, colunaDestinatario, file_path):

    destinatarios = pandas.read_excel(excel_path, usecols=[[colunaDestinatario]])
    print(destinatarios)

    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = uc.Chrome(options=options)
    driver.get('https://conta.uol.com.br/login?t=default')

    emailInput = driver.find_element(By.XPATH, '//*[@id="user"]')
    humanLikeTyping(emailInput, email)

    driver.find_element(By.XPATH, '//*[@id="button-submit"]').click()

    senhaShow = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pass"]')))
    if senhaShow:
        senhaInput = driver.find_element(By.XPATH, '//*[@id="pass"]')
        humanLikeTyping(senhaInput, senha)

    driver.find_element(By.XPATH, '//*[@id="button-submit"]').click()