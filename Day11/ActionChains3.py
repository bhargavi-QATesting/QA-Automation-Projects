from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
driver.maximize_window()
driver.implicitly_wait(5)
action = ActionChains(driver)

slider1 = driver.find_element(By.XPATH, "//div[@id='HTML7']//span[1]")
slider2 = driver.find_element(By.XPATH, "//div[@id='HTML7']//span[2]")
time.sleep(2)
print("Before making changes:",slider1.location, slider2.location) #{'x': 992, 'y': 2067} {'x': 1100, 'y': 2067}

action.drag_and_drop_by_offset(slider1, 25, 0).perform()
action.drag_and_drop_by_offset(slider2, -39, 0).perform()

print("After making changes:",slider1.location, slider2.location) #{'x': 1017, 'y': 2067} {'x': 1060, 'y': 2067}

time.sleep(2)

driver.quit()