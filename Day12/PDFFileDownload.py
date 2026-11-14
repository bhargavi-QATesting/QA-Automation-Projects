from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import  os
location = os.getcwd()


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    #download file in desired location
    preferences = {"download.default_directory":location,"plugins.always_open_pdf_externally":True}  #dict = {"key": value}

    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(service=Service(), options=ops)
    return driver

def edge_setup():
    from selenium.webdriver.edge.service import Service
    #download file in desired location
    preferences = {"download.default_directory":location,"plugins.always_open_pdf_externally":True}  #dict = {"key": value}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option('prefs', preferences)
    driver = webdriver.Edge(service=Service(), options=ops)
    return driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    #settings if we get popup whilw downloading
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2)#0-desktop #1-downloads folder #3-desired location
    ops.set_preference("browser.download.dir", location)
    ops.set_preference("pdfjs.disabled", True) #for pdf
    driver = webdriver.Firefox(service=Service(), options=ops)
    return driver

#driver = chrome_setup()
#driver = edge_setup()
driver = firefox_setup()

driver.get("https://pdfplaceholder.com/sample-pdf-file?utm_source=chatgpt.com")
driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/main/section[1]/ul/li[1]/a/code').click()
time.sleep(5)

driver.quit()



#mime types
#https://www.sitepoint.com/mime-types-complete-list/




#https://www.sreenidhirajakrishnan.com/practice?utm_source=chatgpt.com
#https://jstestingacademy.co.in/qa-demo/?utm_source=chatgpt.com