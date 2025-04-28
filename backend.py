import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def processar(email, senha, excel_path, file_path):

    driver = webdriver.Chrome()
    driver.get('https://conta.uol.com.br/login?t=default')

    driver.find_element(By.XPATH, '//*[@id="user"]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="button-submit"]').click()

    wait = WebDriverWait(driver, 10)
    captcha = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rc-imageselect"]/div[2]/div[1]/div[1]')))

    if captcha:
        print('Deu a porra, apareceu um captcha primo')



