from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ops = webdriver.ChromeOptions()

#prefs = {
    #"profile.default_content_setting_values.notifications": 2
#}
#ops.add_experimental_option("prefs", prefs)

ops.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=ops)

driver.get("https://www.justdial.com/")
#driver.get("https://in.pinterest.com/")
#driver.get("https://in.bookmyshow.com/")
driver.maximize_window()

time.sleep(2)