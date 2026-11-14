from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://blog.vinsguru.com/selenium-webdriver-automating-hoverable-multilevel-dropdowns/")
driver.maximize_window()
driver.implicitly_wait(5)
ele1 = driver.find_element(By.XPATH, '//*[@id="menu-item-3593"]/a/span[1]')
actions = ActionChains(driver)
actions.move_to_element(ele1).perform()


#https://www.spicejet.com/