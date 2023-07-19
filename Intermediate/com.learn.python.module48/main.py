from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver = "C:/chromedriver/chromedriver.exe"

service = Service(executable_path=chrome_driver)
with webdriver.Chrome(service=service) as driver:
    driver.get("https://www.mercadolibre.com.mx/tarjeta-de-video-nvidia-msi-ventus-geforce-rtx-30-series-rtx-3060-geforce-rtx-3060-ventus-2x-12g-oc-oc-edition-12gb/p/MLM17486628")
    elements = driver.find_elements(By.XPATH,
                                    "//*[@id='ui-pdp-main-container']/div[1]/div/div[1]/div[2]/div[3]/div[1]/div[1]/span[1]/span[3]")
    for element in elements:
        value = element.text
        print(value)
    driver.stop_client()
    driver.close()
    driver.quit()
