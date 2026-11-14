from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://testyard.onrender.com/practice/files?utm_source=chatgpt.com")
driver.maximize_window()
time.sleep(5)
fileupload = driver.find_element(By.XPATH, '//*[@id="file-input"]')
fileupload.send_keys("C:/Users/Jagad/Downloads/Kumaran_Systems_JD.pdf")
time.sleep(5)


#Example 2
driver.get("https://testpages.eviltester.com/pages/files/file-upload/")
driver.maximize_window()
fileupload2 = driver.find_element(By.XPATH, '//*[@id="fileinput"]')
fileupload2.send_keys("C:/Users/Jagad/Downloads/Kumaran_Systems_JD.pdf")
time.sleep(5)


driver.quit()

