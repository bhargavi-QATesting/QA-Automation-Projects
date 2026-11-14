from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#accepting simple alert
driver.find_element(By.XPATH, '//*[@id="alertBtn"]').click()
time.sleep(2)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

#confirmation alert with ok and cancel buttons
driver.find_element(By.XPATH, '//*[@id="confirmBtn"]').click()
time.sleep(2)
alert = driver.switch_to.alert
print(alert.text)
alert.dismiss()


#prompt alert with entering text in textbox
driver.find_element(By.XPATH, '//*[@id="promptBtn"]').click()

alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("Bhargavi")
time.sleep(2)
alert.accept()

#example2
driver.get("https://mypage.rediff.com/")
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
time.sleep(1)
driver.switch_to.alert.accept()


