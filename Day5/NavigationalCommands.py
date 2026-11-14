from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
driver.implicitly_wait(5)

driver.back()
driver.implicitly_wait(5)
driver.forward()
driver.implicitly_wait(5)
driver.refresh()
driver.implicitly_wait(5)

driver.quit()