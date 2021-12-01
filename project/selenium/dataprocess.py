from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

import pandas as pd

import time, glob, pickle

#__________________________________

URL = 'https://teachablemachine.withgoogle.com/train/image'

options = Options()
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

def divide_list(l, n): 
    for i in range(0, len(l), n): 
        yield l[i:i + n] 

def run(key,food,menukey):
    root1 = driver.find_element_by_id('tmApp')
    root2 = shadow_element(root1, '#classifier-list')
    add_class = shadow_element(root2, '.add-classes')
    for a in range(3):
        add_class.send_keys('\n')

    for percent in range(5):
        file_path = r'C:\Users\이채은\OneDrive\바탕 화면\포트폴리오\codingcoding\project\selenium\studydata_'+key+"\\"+food+"\\"+str(percent*25) 
        imgs = glob.glob(file_path+'/*')
        root3 = shadow_element(root1, 'tm-classifier-drawer:nth-child('+str(percent+1)+')')
        upload_=shadow_element(root3, '#sample-input-list > button:nth-child(2)')
        upload_.send_keys('\n')
        time.sleep(.1)
        root4 = root3.find_element_by_tag_name('tm-file-sample-input')
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
    time.sleep(3)

    root1 = driver.find_element_by_id('tmApp')
    run_root2=shadow_element(root1,'#run')
    run_root3=shadow_element(run_root2,'#body-container > div.section.no-border > div > div:nth-child(2) > tm-bar-graph')
    run_root4=shadow_element(root1,'#run > tm-file-sample-input')
    select=shadow_element(run_root2,'#select-input')
    time.sleep(20)
    select.send_keys('\n')
    time.sleep(1)
    select.send_keys(Keys.ARROW_DOWN,Keys.ENTER)

    sikpan_upload=shadow_element(run_root4,'#file-input')

    sikpan_pic_path=r"C:\Users\이채은\OneDrive\바탕 화면\포트폴리오\codingcoding\project\selenium\sikpan_"+key+"\\"+food
    source_data=glob.glob(sikpan_pic_path+'/*')
    
    for file in source_data:
        sikpan_upload.send_keys(file)
        print('file',file)
        time.sleep(1)
        for q in range(5):
            run_root3=shadow_element(run_root2,'#body-container > div.section.no-border > div > div:nth-child('+str(q+2)+') ' '> tm-bar-graph')
            individual_result=shadow_element(run_root3,'#value-label')
            menu_result[key][menukey].append(individual_result.text)
            print('결과',individual_result.text)

for key in menu:
    menukey=0
    for foo in menu[key]:
       driver.get(URL)
       run(key,foo,menukey)
       menukey+=1
       input('press enter')

print(menu_result)
with open("result.pkl","wb") as f:
    pickle.dump(menu_result,f)
    input()

with open("result.pkl","rb") as fr:
    menu_result = pickle.load(fr)


real_menu_result={
    "day1":[[],[],[],[],[]],
    "day2":[[],[],[],[],[]]
    }



for key in menu_result:
  a=0
  for menu in menu_result[key]:
    menu = list(divide_list(menu, 5))
    menu_result[key].pop(a)
    menu_result[key].insert(a,menu)
    a+=1

#%제거
for key in menu_result:
  q=0
  for menu in menu_result[key]:
      p=0
      for m in menu:
          a=0
          for number in m:
              number=((number.replace("%","")))
              menu_result[key][q][p].pop(a)
              menu_result[key][q][p].insert(a,int(number))
              a=a+1
          p=p+1
      q=q+1

for key in menu_result:
  a=0
  for menu in menu_result[key]:
   
    for m in menu:
      sum_m=m[0]*0+m[1]*25+m[2]*50+m[3]*75+m[4]*100
      target_m=sum_m/100
      real_menu_result[key][a].append(target_m)
    a+=1

print(menu_result)
print(real_menu_result)

menu={
    "day1":["egg","kimchi","namul","rice","soup"],
    "day2":["hobak","kimchi","potato","rice","soup"]
    }

a=0

for key in real_menu_result:
  for p in real_menu_result[key]:
    file_name=str(a)+'.xlsx'
    df=pd.DataFrame(p)
    df.to_excel(file_name)
    a=a+1