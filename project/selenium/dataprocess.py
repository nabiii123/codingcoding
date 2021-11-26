import selenium
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

#__________________________________

#element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))


URL = 'https://teachablemachine.withgoogle.com/train/image'

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10) # seconds
# wait = WebDriverWait(driver, 10)

menu={
    "day1":["egg","kimchi","namul","rice","soup"],
    "day2":["hobak","kimchi","potato","rice","soup"]
    }

menu_result={
    "day1":[[],[],[],[],[]],
    "day2":[[],[],[],[],[]]
    }

for key in menu:
    menukey=0
    for food in menu[key]:
        driver.get(url=URL)
        add_class=driver.find_element_by_class_name('add-classes')#class 추가
        for a in range(3):
            add_class.click()
        for percent in range(0,101,25):
            file_path=os.listdir('C:₩₩Users₩₩이채은₩₩OneDrive₩₩바탕 화면₩₩포트폴리오₩₩codingcoding₩₩project₩₩studydata_'+key+"₩"+food+str(percent)) #폴더안의 파일 주소 가져오기
            upload_=driver.find_element_by_css_selector("#sample-input-list > button:nth-child(2)")
            upload_.click()
            studydata_input=driver.find_element_by_id("file-input")
            for study in file_path:
                studydata_input.send_keys(study)
        start_study=driver.find_element_by_css_selector("#container > tm-button")
        select = driver.find_element_by_id('select-input')
        select.select_by_visible_text("파일")
        sikpan_upload=driver.find_element_by_id('file-input') #결과도출&리스트 저장
        sikpan_pic_path=os.listdir(".₩₩Users₩₩이채은₩₩OneDrive₩₩바탕 화면₩₩포트폴리오codingcoding₩₩project₩₩studydata_₩₩sikpan_"+key+"₩₩"+food)
        for file in sikpan_pic_path:
            sikpan_upload.send_key(file)
            individual_result=driver.find_elements_by_id("value-label")
            menu_result[key][menukey].append(individual_result)
        menukey=menukey+1
        driver.close()

#%제거
for key in menu_result:
    for n in key:
        for m in n:
            for number in m:
                m=float((m.replace("%","")))

print(menu_result)

#############################################여기부터 colab으로 이동#######

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plot

# #단일 값 만들기
# for key in menu_result:
#     for n in key:
#         np_array=np.array(n)
#         sum_array=np_array.sum(axis=1)
#         target_array=sum_array/100

# #정규분포 그리기&저장
# for key in menu_result:
#     menukey=0
#     for n in key:
#         plt.title(menu[key][menukey]+"의 잔반")
#         plt.hist(n)
#         menukey=menukey+1
#         plt.savefig('.₩₩'+menu[key][menukey]+'sin.png')
