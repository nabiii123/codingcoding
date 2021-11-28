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
# wait = WebDriverWait(driver, 10)

URL = 'https://teachablemachine.withgoogle.com/train/image'

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10) # seconds

menu={
    "day1":["egg","kimchi","namul","rice","soup"],
    "day2":["hobak","kimchi","potato","rice","soup"]
    }

menu_result={
    "day1":[[],[],[],[],[]],
    "day2":[[],[],[],[],[]]
    }

def shadow_element(elem, query):
    return driver.execute_script(f"return arguments[0].shadowRoot.querySelector('{query}')", elem)

for key in menu:
    menukey=0
    for food in menu[key]:
        driver.get(url=URL)

        root1 = driver.find_element_by_id('tmApp')
        root2 = shadow_element(root1, '#classifier-list')
        add_class = shadow_element(root2, '.add-classes')
        for a in range(3):
            add_class.send_keys('\n')

        for percent in range(0,101,25):
            file_path=os.listdir('C:/Users/이채은/OneDrive/바탕 화면/포트폴리오/codingcoding/project/studydata_'+key+"/"+food+"/"+str(percent)) #폴더안의 파일 주소 가져오기
            root3 = shadow_element(root1, 'tm-classifier-drawer:nth-child('+str(menukey+1)+')')
            upload_=shadow_element(root3, '#sample-input-list > button:nth-child(2)')
            upload_.send_keys('\n')
            root4=shadow_element(root3,'tm-file-sample-input')
            exit_button=shadow_element(root3,'#exit-button')
            studydata_input=shadow_element(root4,'#file-input')
            for study in file_path:
                studydata_input.send_keys(study)
                exit_button.send_keys('\n')
                
        study_root2=shadow_element(root1,'#train')
        study_root3=shadow_element(study_root2,'#train-btn')
        start_study=shadow_element(study_root3,'#container > tm-button')
        start_study.send_keys('\n')
        
        run_root2=shadow_element(root1,'#run')
        run_root3=shadow_element(run_root2,'#body-container > div.section.no-border > div > div:nth-child(2) > tm-bar-graph')
        select=shadow_element(run_root2,'#select-input')
        select.select_by_visible_text("파일")
        sikpan_upload=shadow_element(run_root2,'#file-input') #결과도출&리스트 저장
        sikpan_pic_path=os.listdir("./Users/이채은/OneDrive/바탕 화면/포트폴리오codingcoding/project/sikpan_"+key+"/"+food)
        for file in sikpan_pic_path:
            sikpan_upload.send_key(file)
            for q in range(5):
                run_root3=shadow_element(run_root2,'#body-container > div.section.no-border > div > div:nth-child('+str(q+2)+') ' '> tm-bar-graph')
                individual_result=shadow_element(run_root3,'#value-label')
                menu_result[key][menukey].append(individual_result)
        menukey=menukey+1
        driver.close()

# #%제거
# for key in menu_result:
#     for n in key:
#         for m in n:
#             for number in m:
#                 m=float((m.replace("%","")))

print(menu_result)

# ######여기부터 colab으로 이동#######

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
#         plt.savefig('./'+menu[key][menukey]+'sin.png')
