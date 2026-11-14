from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://text-compare.com/")
driver.maximize_window()

#CTRL+A
#CTRL+C
#TAB
#CTRL+V
element1 = driver.find_element(By.ID, "inputText1")
element1.send_keys("Python")
element2 = driver.find_element(By.ID, "inputText2")

actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
actions.send_keys(Keys.TAB).perform()
actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

print(element1.get_attribute("value"))
print(element2.get_attribute("value"))

time.sleep(2)

driver.quit()


