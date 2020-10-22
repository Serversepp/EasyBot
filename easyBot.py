try:
    from selenium import webdriver
    pass

except:
    print("error try pip install selenium")
    raise



def makechromebot(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        pass
    except Exception as e:
        print("Task failed")
        driver = "001"
        raise

    return driver

def clickatxp(driver,xp):
    driver.find_element_by_xpath(xp).click()
    pass

def fillatxp(driver,xp,payload):
    driver.find_element_by_xpath(xp).send_keys(payload)
    pass

def changepage(driver,url):
    driver.get(url)
    pass
