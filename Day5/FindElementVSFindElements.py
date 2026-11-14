from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.python.org/downloads/")
driver.maximize_window()
driver.implicitly_wait(5)

#driver.find_element(By.XPATH, "//a[normalize-space()='PSF']").click()
#driver.implicitly_wait(5)
#print(driver.title)

#links = driver.find_element(By.XPATH, "//div[@class='main-footer-links']//a")
#print(links.text)

links = driver.find_elements(By.XPATH, "//div[@class='main-footer-links']//a")
print(len(links))
print(links[0].text)

for link in links:
    print(link.text)



#NoSuchElementException
#driver.find_element(By.LINK_TEXT, "Don")




driver.quit()