from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import yaml

with open("words.yaml", "r") as file:
    words = yaml.load(file, Loader=yaml.FullLoader)

driver = webdriver.Firefox()
driver.get("https://quizlet.com/594116128/match")
time.sleep(1)
button_ok = driver.find_element_by_class_name("UIButton--hero")
webdriver.ActionChains(driver).click(button_ok).perform()
time.sleep(0.05)
de_elements = driver.find_elements_by_class_name("lang-de")
for e in de_elements:
    webdriver.ActionChains(driver).click(e).perform()
    fr_text = words[e.text]
    fr_element = driver.find_element_by_xpath(f"//*[text() = \"{fr_text}\"]")
    webdriver.ActionChains(driver).click(fr_element).perform()
