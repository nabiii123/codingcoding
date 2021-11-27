import selenium
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-classes')))

URL = 'https://teachablemachine.withgoogle.com/train/image'

driver.get(url=URL)
# add_class=driver.find_element_by_class_name('add-classes')#class 추가
element = wait.until(EC.element ((By.CLASS_NAME, 'add-classes')))
element.click()