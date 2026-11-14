from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#about XPATH from selectorhub
driver = webdriver.Chrome()
driver.get("https://automationexercise.com/#google_vignette")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a').click()
#same webelement xpaths from right click and selectorhub
#driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div[1]/form/input[2]').click()
#driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys("abc@gmail.com")

#using or operator with xpath
#driver.find_element(By.XPATH,"//input[@name='password' or @xpath='2']").send_keys("abc")

#using and operator with xpath
#driver.find_element(By.XPATH,"//input[@name='password' and @placeholder='Password']").send_keys("abc")

#using contains() operator
#driver.find_element(By.XPATH,"//input[contains(@placeholder,'email')]").send_keys("email@gmail.com")

#using starts-with() operator
#driver.find_element(By.XPATH,"//input[starts-with(@placeholder,'Your')]").send_keys("abc@gmail.com")

#using text() operator
title = driver.find_element(By.XPATH,"//h2[text()='Login to your account']")
print(title.text)

driver.implicitly_wait(5)
driver.save_screenshot("screenshot2.png")


driver.quit()
