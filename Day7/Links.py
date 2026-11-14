from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.devtools.v153.dom import get_attributes

driver = webdriver.Chrome()
driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")
driver.maximize_window()

#click on link
#driver.find_element(By.LINK_TEXT,"Exercises").click()
#time.sleep(2)

links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))

for link in links:
    print(link.text)
    print(link.get_attribute("href"))

driver.get("https://the-internet.herokuapp.com")

links1 = driver.find_elements("tag name", "a")
print(len(links1))

for i in links1:
    print(i.get_attribute("href"))
    print(i.text)


driver.quit()