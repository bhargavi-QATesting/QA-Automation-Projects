from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v153.dom import get_attributes

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

namefield = driver.find_element(By.XPATH, "//label[normalize-space()='Name:']")
print(namefield.text)
print(namefield.get_attribute("value"))

username = driver.find_element(By.ID,"email")
username.click()
username.send_keys("bhargavi@gmail.com")
print(username.text)
print(username.get_attribute('value'))