from selenium import webdriver


def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless=new")
    driver = webdriver.Chrome(service=Service(),options=ops)
    return driver

def headless_edge():
    from selenium.webdriver.edge.service import Service
    ops = webdriver.EdgeOptions()
    ops.add_argument("--headless=new")
    driver = webdriver.Edge(service=Service(),options=ops)
    return driver

def headless_firefox():
    from selenium.webdriver.firefox.service import Service
    ops = webdriver.FirefoxOptions()
    ops.add_argument("--headless=new")
    driver = webdriver.Firefox(service=Service(),options=ops)
    return driver

#driver = headless_chrome()
#driver = headless_edge()
driver = headless_firefox()
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html#")
print(driver.title)
print(driver.current_url)

driver.quit()