import os
import base64
import time
import requests
import pandas as pd
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException

def setup_driver():
    """Configura e retorna o driver do Selenium."""
    return webdriver.Firefox()

def search_google(driver, query):
    """Realiza uma pesquisa no Google e retorna a primeira página de resultados."""
    driver.get('http://www.google.com')
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Considerar o uso de esperas explícitas aqui

def get_first_result_data(driver, chave):
    """Obtém o título e a URL do primeiro resultado de pesquisa do Google."""
    try:
        first_result = driver.find_element(By.XPATH, '//div[contains(@class, "tF2Cxc")]')
        link = first_result.find_element(By.TAG_NAME, 'a')
        titulo = link.find_element(By.TAG_NAME, 'h3').text
        url = link.get_attribute('href')
        return titulo, url
    except NoSuchElementException:
        print(f"Não foi possível encontrar o resultado para a chave '{chave}'")
        return "", ""

def download_images(driver, chave):
    """Baixa as primeiras 5 imagens de uma pesquisa no Google Images."""
    driver.get(f'https://www.google.com/search?q={chave}&tbm=isch')
    time.sleep(2)  # Considerar o uso de esperas explícitas aqui
    images = driver.find_elements(By.XPATH, '//img[contains(@class, "rg_i")]')
    os.makedirs(f'./output/{chave}', exist_ok=True)

    for i, img in enumerate(images[:5]):
        img_url = img.get_attribute('src')
        save_image(img_url, f'./output/{chave}/{str(i+1).zfill(3)}.jpg')

def save_image(data, path):
    """Salva uma imagem a partir de uma URL ou dados em base64."""
    try:
        if data.startswith('http'):
            response = requests.get(data)
            if response.status_code == 200:
                with open(path, 'wb') as file:
                    file.write(response.content)
        elif data.startswith('data:image'):
            header, encoded = data.split(',', 1)
            data = base64.b64decode(encoded)
            with open(path, 'wb') as file:
                file.write(data)
    except requests.RequestException as e:
        print(f"Erro ao baixar a imagem: {e}")


def main():
    """Função principal do script."""
    df = pd.read_csv('./input/pesquisa.csv')
    driver = setup_driver()
    results = []

    for chave in tqdm(df['Chave'], desc='Processando', unit='chave'):
        search_google(driver, chave)
        titulo, url = get_first_result_data(driver, chave)
        results.append([chave, titulo, url])
        download_images(driver, chave)

    pd.DataFrame(results, columns=['Chave', 'Título', 'URL']).to_csv('output.csv', index=False)
    driver.quit()


if __name__ == "__main__":
    main()
