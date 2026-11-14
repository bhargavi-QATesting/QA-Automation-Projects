from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests as requests
from selenium.webdriver.common.devtools.v153.dom import get_attributes

#BrokenLinks
#<=400 error codes ex: 404 page not found error
#we need to install requests package from file->settings->PythonInterpreter->+->requests

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()


brokenlink = driver.find_elements(By.TAG_NAME,"a")
print(len(brokenlink))
count = 0

for i in brokenlink:
    url = i.get_attribute("href")
    try:
        res = requests.head(url)  #request module hit to the server in the backend so links will not open while execution(sending request directly to the server)
    except:
        None

    if res.status_code>=400:
        print(url, " is broken link")
        count+=1
    else:
        print(url, " is good link")
print("Total no of broken links:", count)
driver.quit()


