from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("Python")

driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)

searchresults = driver.find_elements(By.XPATH, '//*[@id="wikipedia-search-result-link"]/a')

for result in searchresults:
    print(result.text)

for i in searchresults:
    i.click()
    print(driver.title)

time.sleep(2)

for window in driver.window_handles:
    driver.switch_to.window(window)
    print(driver.title)

time.sleep(2)

driver.quit()
#use above url click on textbox under W enter any text and click on search
#after searching capture all the values from results
#switch to each browser window and after getting all browser windows, print each browser window title
#after capturing close all the windows