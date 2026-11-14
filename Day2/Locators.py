from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()
driver.find_element(By.XPATH, '//i[@class="material-icons card_travel"]').click()
driver.implicitly_wait(5)
#driver.find_element(By.LINK_TEXT, " Products").click()
driver.save_screenshot("screenshot1.png")
links1 = driver.find_elements(By.TAG_NAME, "iframe")
print(len(links1))
driver.implicitly_wait(5)

Title1 = driver.title
print(Title1)
print(len(Title1))


driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(5)
driver.find_element(By.CLASS_NAME, "title")
links2 = driver.find_elements(By.TAG_NAME, "a")
print(len(links2))

Title2 = driver.title
print(Title2)
print(len(Title2))

if Title1 == Title2 and links1 == links2:
    print("Count is matching")
else:
    print("Count is not matching")

driver.quit()