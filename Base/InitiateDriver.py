from selenium import webdriver
from selenium.webdriver.common.by import By
from Library import ConfigReader


from selenium import webdriver
import time
from selenium.webdriver.common.by import By



def startbrowser():
    global driver
    driver = webdriver.Chrome()
    driver.get(ConfigReader.readConfigdata("AccessWebsite","website_url"))
    driver.maximize_window()
    driver.implicitly_wait(7)
    originalwindow = driver.current_window_handle
    driver.find_element(By.XPATH, "/html/body/header/div/nav/div[2]/a").click()
    driver.implicitly_wait(7)
    #driver.execute_script("window.scrollTo(0, 500);")
    driver.implicitly_wait(7)
# login screen redirect
    active_window_ids = driver.window_handles
    for windows in active_window_ids:
        if windows!=originalwindow:
            driver.switch_to.window(windows)
            driver.find_element(By.XPATH,"/html/body/section/div/div/div/div/div/div/div[2]/div/form/div[5]/p/a").click()
            abc = driver.current_url
            if abc.endswith("user/signup"):
                print("we are on the correct page")
    return driver

def closebrowser():
    driver.close()