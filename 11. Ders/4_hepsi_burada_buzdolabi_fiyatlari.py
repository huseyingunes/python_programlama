import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.hepsiburada.com/")
action = webdriver.ActionChains(driver)
time.sleep(5)
dgm_kabul_et = driver.find_element(By.ID, "onetrust-accept-btn-handler")
dgm_kabul_et.click()

elm_elektronik = driver.find_element(By.XPATH,
                                     '//*[@id="NavigationDesktop_2bc95b71-00d3-4b56-8b06-8f9cb3f65127"]/div/div/div/div/div[1]/div/ul/li[1]')
action.move_to_element(elm_elektronik)
action.perform()
