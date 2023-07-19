from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By

chrome_driver = "C:/chromedriver/chromedriver.exe"
service = Service(executable_path=chrome_driver)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
element = driver.find_element(By.XPATH, "//*[@id='articlecount']/a[1]")
print(element.text)
element.click()
search_button = driver.find_element(By.XPATH, "//*[@id='searchform']/div")
ActionChains(driver)\
        .move_to_element(search_button)\
        .pause(1)\
        .click_and_hold()\
        .pause(1)\
        .send_keys("Python")\
        .send_keys(Keys.ENTER)\
        .perform()
ActionBuilder(driver).clear_actions()


# Alternative
# article_count = driver.find_elements(By.CSS_SELECTOR,"#articlecount a")
# for element in article_count:
#     print(element.text)
# driver.stop_client()
# driver.close()
# driver.quit()
