import undetected_chromedriver as webdriver
#from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import csv
import time
import random

options = webdriver.ChromeOptions()
profile = "/Users/mac/Library/Application Support/Google/Chrome/User Data/Profile 3"
options.add_argument(f"user-data-dir={profile}")
driver = webdriver.Chrome(options=options, version_main=109)

driver.maximize_window()

driver.get('https://www.google.com/?gl=us&hl=en')



csvFileName = 'YOUR_FILENAME'
with open('/Users/mac/Work/Python/Data/'+csvFileName+'.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    i=1
    r = 0
    rows= reader
    for i in range(1, 100):
    
        for row in rows:

            r = random.randint(1, 3)
            if i>1 and r == 1 :
                driver.refresh()
                time.sleep(5)
                driver.find_element(By.NAME,"q").clear()
            else:
                driver.get('https://www.google.com/?gl=us&hl=en')


            time.sleep(5)
            search = str(row[0])
            #options.add_argument("--headless")     
            driver.implicitly_wait(3)

        
            #scrollRan= random.randint(1222, 2111)
            driver.execute_script("window.scrollTo(0, 3333);")
            #time.sleep(1)
            driver.find_element(By.NAME,"q").send_keys(search + Keys.ENTER)
            time.sleep(3)


            #Click Menu type PAA
            downButton = driver.find_element(By.CSS_SELECTOR,"#smin-serp-widget > div.smin-serp-widget-inner > div:nth-child(1) > div.smin-serp-widget-tools > select.smin-serp-widget-select.smin-serp-widget-select-target")
            downButton.click()
            time.sleep(1)

            #Click type PAA
            downButton = driver.find_element(By.CSS_SELECTOR,"#smin-serp-widget > div.smin-serp-widget-inner > div:nth-child(1) > div.smin-serp-widget-tools > select.smin-serp-widget-select.smin-serp-widget-select-target > option:nth-child(19)")
            downButton.click()
            time.sleep(1)

            #Click Menu Copy
            downButton = driver.find_element(By.CSS_SELECTOR,"#smin-serp-widget > div.smin-serp-widget-inner > div:nth-child(1) > div.smin-serp-widget-tools > select.smin-serp-widget-select.smin-serp-widget-select-action")
            downButton.click()
            time.sleep(1)

            #CLICK COPY
            copyButton = driver.find_element(By.CSS_SELECTOR,"#smin-serp-widget > div.smin-serp-widget-inner > div:nth-child(1) > div.smin-serp-widget-tools > select.smin-serp-widget-select.smin-serp-widget-select-action > option:nth-child(2)")
            copyButton.click()
            time.sleep(5)
            #CLICK GO
            
            goButton = driver.find_element(By.CSS_SELECTOR,"#smin-serp-widget > div.smin-serp-widget-inner > div:nth-child(1) > div.smin-serp-widget-tools > button")
            goButton.click()
            #wait till element is visible
            #WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#smin-serp-widget-status")))
            time.sleep(13)

            

            #WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
            #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()




            df = pd.read_clipboard(names=["PAA Title", "Parent", "Text", "URL", "URL Title"])
        
            #Organize df elements in a list

            cc=0
            PAA_List = []
            textList = []
            PAA_List2 = []
            textList2 = []

            if pastQuestion == df["PAA Title"][0]: 
                print("Duplicate questions...Retrying")

            else:
                pastQuestion = df["PAA Title"][0]
                for index, row in df.iterrows():
                    if cc < 70:
                        PAA_List.append(row["PAA Title"])
                        textList.append(row["Text"])
                    else:
                        PAA_List2.append(row["PAA Title"])
                        textList2.append(row["Text"])
                    cc+=1






                row1 = zip(PAA_List, textList)
                #row2 = zip(PAA_List2, textList2)
                header = [search,"NEW GROUP"]

                with open('/Users/mac/Work/Python/Data/'+ csvFileName+ '_PAA.csv', 'a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                    writer.writerows(row1)


                with open('/Users/mac/Work/Python/Data/'+csvFileName+' COUNT.txt', 'w') as txtFile:
                    txtFile.write('\n'+str(i))
                    #print(i)            


                if PAA_List[0]=="":
                    print("no list")
                else:
                    data = pd.read_csv('/Users/mac/Work/Python/Data/'+csvFileName+'.csv')
                    #data = data.drop(labels=0, axis=0)
                    data = data.drop(data.index[0])
                    #print("KW REMOVED!")
                    #close data file
                    data.to_csv('/Users/mac/Work/Python/Data/'+csvFileName+'.csv', index=False)
                

                
                i+=1
                time.sleep(1)