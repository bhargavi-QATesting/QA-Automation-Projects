from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
# driver.get("https://www.google.com")
# driver.maximize_window()
# driver.find_element(By.NAME,"q").send_keys("Virat kohli")
# time.sleep(3)

# driver.get("https://www.youtube.com")
# driver.maximize_window()
# time.sleep(3)
# print("Title:",driver.title)

# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)

# driver.get("https://proleed.academy/exercises/selenium/automation-practice-form-with-radio-button-check-boxes-and-drop-down.php")

# #radio buttons
# pension = driver.find_element(By.ID, "pension")
# driver.execute_script("arguments[0].click();", pension)

# #textbox
# driver.find_element(By.XPATH,'//*[@id="mothername"]').send_keys("pushpa")

# #checkboxes
# checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

# driver.execute_script("arguments[0].click();", checkboxes[0])
# driver.execute_script("arguments[0].click();", checkboxes[2])
# time.sleep(2)

# #dropdowns
# month = Select(driver.find_element(By.ID,"dob_month"))
# month.select_by_visible_text("March")
# date = Select(driver.find_element(By.ID,"dob_date"))
# date.select_by_visible_text("13")
# year = Select(driver.find_element(By.ID,"dob_year"))
# year.select_by_visible_text("2000")
# time.sleep(5)

# driver.get("https://www.youtube.com/results?search_query=virat+kohli")
# links = driver.find_elements(By.TAG_NAME,"a")

# for i in links:
    # print(i.text)

#Alert
driver.get("https://testautomationpractice.blogspot.com/")
#driver.find_element(By.XPATH,'//*[@id="alertBtn"]').click()
driver.find_elements(By.CLASS_NAME, "title")
Title = driver.title
print(Title)
# alert = driver.switch_to.alert
# time.sleep(2)
# print(alert.text)
# alert.accept()
# time.sleep(2)

#doubleclick
# action = ActionChains(driver)
# ele = driver.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')
# action.double_click(ele).perform()
# action.context_click(ele).perform()
# time.sleep(3)


#draganddrop
s = driver.find_element(By.ID,"draggable")
d = driver.find_element(By.ID,"droppable")
action = ActionChains(driver)
action.drag_and_drop(s,d).perform()
time.sleep(2)

driver.quit()


