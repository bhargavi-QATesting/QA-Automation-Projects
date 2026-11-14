from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import  os
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(10)
#driver.save_screenshot("screenshot1.png")
#or
#driver.save_screenshot("C:\\Users\\Jagad\\PycharmProjects\\PythonLearning\\pythonProject\\Day13\\Orangehrm.png")
#or
#driver.save_screenshot(os.getcwd()+"\\ORANGEHRMPAGE.png")
#or
#driver.get_screenshot_as_file("file.png")
#or
driver.get_screenshot_as_file(os.getcwd()+"\\Bhargavifile.png")

#driver.get_screenshot_as_png() and driver.get_screenshot_as_base64() #stores or saves screenshot in binary format