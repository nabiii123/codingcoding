import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import os

#__________________________________

URL = 'https://teachablemachine.withgoogle.com/train/image'

# driver = webdriver.Chrome(executable_path='chromedriver')
# driver.get(url=URL)

# add_class=driver.find_element_by_id("add-classes")
# for a in range(3):
#     add_class.click()

# menu={
#     "day1":["egg","kimchi","namul","rice","soup"],
#     "day2":["hobak","kimchi","potato","rice","soup"]
#     }

def fileroot():
    dir_path = "Users\이채은\OneDrive\바탕 화면\codingcoding\project\studydata_day1\rice"
    # +day+"/"+menu["day"+day][n]
    for (root, directories, files) in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)


fileroot()
