import time
from PIL import Image
import pytesseract

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.hepsiburada.com/")
action = webdriver.ActionChains(driver)
time.sleep(5)
#dgm_kabul_et = driver.find_element(By.ID, "onetrust-accept-btn-handler")
#dgm_kabul_et.click()

bgl_tum_utuler = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[5]/div[3]/div/div/div/div/div/div/div[1]/div/ul/li[1]')
action.move_to_element(bgl_tum_utuler)
action.perform()
