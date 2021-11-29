import selenium
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os, time, glob

#__________________________________

#element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
# wait = WebDriverWait(driver, 10)

URL = 'https://teachablemachine.withgoogle.com/train/image'

options = Options()
# options.add_experimental_option("prefs", {
#     "profile.default_content_setting_values.notifications": 1
# })
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10) # seconds
wait = WebDriverWait(driver, 10)

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

driver.get(URL)
for key in menu:
    menukey=0
    for food in menu[key]:

        root1 = driver.find_element_by_id('tmApp')
        root2 = shadow_element(root1, '#classifier-list')
        add_class = shadow_element(root2, '.add-classes')
        for a in range(3):
            add_class.send_keys('\n')

        for percent in range(5):
            file_path = 'C:/Users/이채은/OneDrive/바탕 화면/포트폴리오/codingcoding/project/studydata_'+key+"/"+food+"/"+str(percent*25) #폴더안의 파일 주소 가져오기
            imgs = glob.glob(file_path+'/*')
            root3 = shadow_element(root1, 'tm-classifier-drawer:nth-child('+str(percent+1)+')')
            upload_=shadow_element(root3, '#sample-input-list > button:nth-child(2)')
            upload_.send_keys('\n')
            time.sleep(.1)
            root4 = root3.find_element_by_tag_name('tm-file-sample-input')
            # root4 = shadow_element(root1,'tm-file-sample-input:nth-child('+str(menukey+1)+')')
            exit_button=shadow_element(root3,'#exit-button')
            studydata_input=shadow_element(root4,'#file-input')
            for study in imgs:
                studydata_input.send_keys(study)
                time.sleep(.1)
            exit_button.send_keys('\n')

        study_root2=shadow_element(root1,'#train')
        study_root3=shadow_element(study_root2,'#train-btn')
        start_root4=shadow_element(study_root3,'#container > tm-button')
        start_study=shadow_element(start_root4,'button')

        time.sleep(2)
        start_study.send_keys('\n')
        
        time.sleep(60)
        run_root2=shadow_element(root1,'#run')
        run_root3=shadow_element(run_root2,'#body-container > div.section.no-border > div > div:nth-child(2) > tm-bar-graph')
        select=Select(shadow_element(run_root2,'#select-input'))
        select.select_by_visible_text('파일')
        time.sleep(.1)
        sikpan_upload=shadow_element(run_root2,'#file-input') #결과도출&리스트 저장
        sikpan_pic_path="C:/Users/이채은/OneDrive/바탕 화면/포트폴리오codingcoding/project/sikpan_"+key+"/"+food
        source_data=glob.glob(sikpan_pic_path+'/*')
        print(source_data)
        for file in source_data:
            sikpan_upload.send_keys(file)
            for q in range(5):
                run_root3=shadow_element(run_root2,'#body-container > div.section.no-border > div > div:nth-child('+str(q+2)+') ' '> tm-bar-graph')
                time.sleep(1)
                individual_result=shadow_element(run_root3,'#value-label')
                menu_result[key][menukey].append(individual_result)
                print(menu_result)

        menukey=menukey+1
        driver.refresh()
        try:
            result= driver.switch_to_alert()
            result.accept()
        except:
            "there is no alert"
        time.sleep(5)

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
