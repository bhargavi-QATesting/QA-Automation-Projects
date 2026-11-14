from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

"""driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.switch_to.frame("SingleFrame")
driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("bhargavi") #doing action in frame
time.sleep(2)

driver.switch_to.default_content()
webtable = driver.find_element(By.LINK_TEXT, "WebTable")
webtable.click()
time.sleep(2)

print(webtable.text)"""

#example 2
"""driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.maximize_window()

# Enter top frame first
driver.switch_to.frame("frame-top")

# Left frame
driver.switch_to.frame("frame-left")
print(driver.find_element(By.TAG_NAME, "body").text)

# Return to frame-top
driver.switch_to.parent_frame()

# Middle frame
driver.switch_to.frame("frame-middle")
print(driver.find_element(By.ID, "content").text)

# Return to frame-top
driver.switch_to.parent_frame()

# Right frame
driver.switch_to.frame("frame-right")
print(driver.find_element(By.TAG_NAME, "body").text)

# Return to main page
driver.switch_to.default_content()

# Bottom frame
driver.switch_to.frame("frame-bottom")
print(driver.find_element(By.TAG_NAME, "body").text)"""

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()
time.sleep(2)

outerframe = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

innerframe = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Bhargavi")
time.sleep(2)

driver.switch_to.default_content()
driver.find_element(By.XPATH, "//a[normalize-space()='WebTable']").click()



driver.quit()