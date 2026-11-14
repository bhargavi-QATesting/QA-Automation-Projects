from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# To find multiple webelements
driver = webdriver.Edge()
driver.get("https://automationexercise.com/")
driver.maximize_window()
driver.implicitly_wait(5)
sliders = driver.find_elements(By.CLASS_NAME, "col-sm-6")
print(len(sliders))

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

if(len(sliders)==6):
    print("There are 6 sliders")
else:
    print("There are no 6 sliders")

driver.quit()

