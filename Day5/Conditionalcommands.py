from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


username = driver.find_element(By.ID, "name")
print(username.is_displayed())
print(username.is_enabled())

checkbox = driver.find_element(By.XPATH, "//input[@id='sunday']")
checkbox.click()
print(checkbox.is_selected())
radio_button = driver.find_element(By.XPATH, "//input[@id='female']")
radio_button.click()
print(radio_button.is_selected())

driver.implicitly_wait(5)
driver.quit()