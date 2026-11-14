from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v153.dom import get_attributes
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
#driver.implicitly_wait(5)
webwait = WebDriverWait(driver, 10)

searchkey = driver.find_element(By.NAME, "q")
searchkey.send_keys("virat_kohli")
searchkey.submit()

searchlink=webwait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='virat_kohli")))
searchlink.click()

driver.find_element(By.XPATH, "//h3[@id='_YH3oasiBIuCUhvcPrZbcgQ8_172']").click()
driver.quit()