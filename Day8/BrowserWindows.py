from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#Approach 1 (if we have just 1,2 browser windows)
'''driver.find_element(By.XPATH, '//*[@id="HTML4"]/div[1]/button').click()
print(driver.title)
driver.switch_to.window(driver.window_handles[1])
print(driver.window_handles[0])
print(driver.window_handles[1])

driver.find_element(By.XPATH, '//*[@id="PageList1"]/div/ul/li[9]/a').click()
print(driver.title)'''

'''driver.get("https://www.pavantestingtools.com/")
driver.maximize_window()

windowid = driver.current_window_handle
print(windowid)'''

#Approach 2 (if we have multiple browser windows) use looping statement
'''driver.find_element(By.XPATH, '//*[@id="HTML4"]/div[1]/button').click()
driver.switch_to.window(driver.window_handles[1])
for winid in driver.window_handles:
    driver.switch_to.window(winid)
    print(driver.title)'''

#Approach 3 (to close specific browser windows of our choice)
driver.find_element(By.XPATH, '//*[@id="HTML4"]/div[1]/button').click()
driver.switch_to.window(driver.window_handles[1])
for winid in driver.window_handles:
    driver.switch_to.window(winid)
    if driver.title == "Automation Testing Practice":  #which browser you want to close use that browser title
        driver.close()



time.sleep(2)