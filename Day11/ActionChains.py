from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
driver.maximize_window()
driver.implicitly_wait(5)
action = ActionChains(driver)

#MouseHover
mousehover = driver.find_element(By.XPATH, '//*[@id="HTML3"]/div[1]/div/button')
mousehover2 = driver.find_element(By.XPATH, '//*[@id="HTML3"]/div[1]/div/div/a[1]')
mousehover3 = driver.find_element(By.XPATH, '//*[@id="HTML3"]/div[1]/div/div/a[2]')
time.sleep(2)
action.move_to_element(mousehover).move_to_element(mousehover2).move_to_element(mousehover3).click().perform()
time.sleep(2)

#Drag and Drop
draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")
action.drag_and_drop(draggable, droppable).perform()

#DoubleClick
doubleclick = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
action.double_click(doubleclick).perform()

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

#RightClick
rightclick = driver.find_element(By.XPATH, '/html/body/main/p/span')
action.context_click(rightclick).perform()

driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click()
driver.switch_to.alert.accept()


time.sleep(2)
driver.quit()



'''actions.move_to_element(element).perform()      # Mouse Hover
actions.context_click(element).perform()       # Right Click
actions.double_click(element).perform()        # Double Click
actions.click(element).perform()               # Click
actions.drag_and_drop(src,dst).perform()       # Drag and Drop'''