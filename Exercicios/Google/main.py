import time
import base64
import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from log import log_wrapper

class GoogleSearchModel:
    def __init__(self, key):
        self.key = key
        self.results = []

class GoogleSearchController:
    def __init__(self, model):
        self.model = model

    @log_wrapper
    def search_google(self):
        try:
            driver.get(f'https://www.google.com/search?q={self.model.key}&sca_esv=597319875&tbm=isch&sxsrf=ACQVn0-rrny6-PPoIIK8NK8sVFgrMqjDuQ:1704932253586&source=lnms&sa=X&ved=2ahUKEwi86NzKh9SDAxXYppUCHVlJC3YQ_AUoAnoECAEQBA&biw=1536&bih=695&dpr=1.25')
            time.sleep(1.5)
        except Exception as e:
            raise(f"Error during Google search: {e}")

    @log_wrapper
    def capture_google_data(self):
        try:
            rows = driver.find_elements(By.XPATH, "//a[@jsname='uy6ald']")
            for row in rows:
                url = row.get_attribute("href")
                title = row.get_attribute("aria-label")
                data = {
                    "chave": self.model.key,
                    "titulo": title,
                    "url": url
                }
                self.model.results.append(data)
        except Exception as e:
            raise(f"Error during capturing Google data: {e}")

    @log_wrapper
    def capture_images(self):
        try:
            self.create_output_folder()
            rows = driver.find_elements(By.XPATH, "//img[@jsname='Q4LuWd']")

            for i, row in enumerate(rows[0:5], start=1):
                src = row.get_attribute("src")

                if src and src.startswith("data:image"):
                    base64_str = str(src).split(",")[1]
                    binary = base64.b64decode(base64_str)
                    file_name = f"./output/{self.model.key}/{i:03d}.png"
                    with open(file_name, "wb") as f:
                        f.write(binary)
        except Exception as e:
            raise(f"Error during capturing images: {e}")

    @log_wrapper
    def create_output_folder(self):
        try:
            output_folder = f'./output/{self.model.key}'
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
        except Exception as e:
            raise(f"Error during creating output folder: {e}")

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-logging')
    options.add_argument("--log-level=3")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        input_file = './input/pesquisa.csv'
        output_file = './output/output.csv'
        search_results = []

        with open(input_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)

            for line in reader:
                key = line[0]
                google_search_model = GoogleSearchModel(key)
                google_search_controller = GoogleSearchController(google_search_model)

                google_search_controller.search_google()
                google_search_controller.capture_google_data()
                google_search_controller.capture_images()

                search_results.extend(google_search_model.results)

        with open(output_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['chave','titulo', 'url'])
            for item in search_results:
                writer.writerow([item['chave'], item['titulo'], item['url']])
    except Exception as e:
        raise(f"An unexpected error occurred: {e}")
    finally:
        driver.quit()
