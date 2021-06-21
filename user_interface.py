import streamlit as st
import streamlit.components.v1 as components
def local_css(filename):
    with open(filename) as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)       
local_css('style.css')

components.html("<html><body><h2>VISUALIZATION OF YOUR FITNESS DATA</h2></body></html>")
def main():
    # MENU HAS THREE LISTS ELEMENT
    menu=["Your Latest Visualization Update","Visualize your data","File selector to view data"]
    
    choice=st.sidebar.selectbox("Menu",menu)
    
    if choice=="Your Latest Visualization Update":
        # GET USERNAME AND PASSWORD
        username = st.sidebar.text_input("Enter Mi account email")     
        password = st.sidebar.text_input("Password", type='password')
        
        if st.sidebar.button("Login"):
            # importing all the libraries...
            from selenium import webdriver
            from selenium.webdriver.common.keys import Keys
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            import time
            import re
            from datetime import date
            from PIL import Image
            import pyperclip
            import streamlit.components.v1 as components  
            import glob
            import os
            import pandas as pd
            import matplotlib.pyplot as plt
            import numpy as np
            import plotly.express as px
            from plotly.subplots import make_subplots
            import plotly.graph_objects as go

            
            progress=st.progress(0)
            q=100
            #options = webdriver.ChromeOptions()
            #options.add_argument("headless")
            #options.add_argument("-disable-gpu")
        
            driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
            #driver = webdriver.PhantomJS()
                # driver=webdriver.Edge(executable_path="C:\Program Files (x86)\Driver\msedgedriver.exe")
                # driver=webdriver.Firefox(executable_path="C:\Program Files (x86)\geckodriver.exe")
                # driver=webdriver.Ie(executable_path="C:\Program Files (x86)\IEDriverServer.exe")
            

            # ACCESSING THE WEBSITE
            driver.get("https://user.huami.com/privacy/index.html#/")
            print(driver.title) # title of the page
            print(driver.current_url)
            progress.progress(q-90)
            #----------------------------------------------------
            WAIT_ELEMENT=30
            XPATH_VALUE= "//*[@id=\"chooseOpt\"]/div/div[4]"
            x=WebDriverWait(driver, WAIT_ELEMENT).until(EC.presence_of_element_located((By.XPATH, XPATH_VALUE)))  
            x.click()    
            #----------------------------------------------------

            driver.find_element_by_id("step1").click()
            
            #----------------------------------------------------
            driver.find_element_by_xpath("//*[@id=\"login3Link\"]/li[5]/form/button").click()
            #----------------------------------------------------
            # PUTTING THE USERNAME AND PASSWORD IN GMAIL SCRIPT...
            Phone_number=username
            email_field = driver.find_element_by_id("identifierId")
            email_field.send_keys(Phone_number)

            email_next_button =driver.find_element_by_id("identifierNext")
            email_next_button.click()
            progress.progress(q-80)
            time.sleep(5)

            password_field = driver.find_element_by_name("password")
            password_field.send_keys(password)

            password_next_button = driver.find_element_by_id("passwordNext")
            password_next_button.click()
            
            #----------------------------------------------------
            # SELECT ALL RADIO BUTTONS IN THE WEBSITE
            time.sleep(3)
            WAIT_ELEMENT=30
            for i in range(1,7):
                XPATH_VALUE= f"//*[@id=\"clearData\"]/li[{i}]/span[1]/img[1]"
                y=WebDriverWait(driver, WAIT_ELEMENT).until(EC.presence_of_element_located((By.XPATH, XPATH_VALUE)))  
                y.click()
            #-----------------------------------------------------
            # SELECTING DATE
            driver.find_element_by_xpath("//*[@id=\"to\"]/div[1]/div/input").click()
            progress.progress(q-70)
            todays_date = date.today()
            clicks=(todays_date.month)-1
            for i in range(clicks):
                driver.find_element_by_xpath("//*[@id=\"to\"]/div[2]/div[2]/div/div/button[1]").click()

            driver.find_element_by_xpath("//*[@id=\"to\"]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[4]").click()
            #--------------------------------------------------------
            driver.find_element_by_xpath("//*[@id=\"dateConfigBox\"]/div[1]/div/input").click()

            driver.find_element_by_xpath("//*[@id=\"dateConfigBox\"]/div[1]/div/input").send_keys(Keys.ENTER)
            #-------------------------------------------------------
            driver.find_element_by_id("ok").click()
            #------------------------------------------------------
            # AGAIN PUTTING THE USERNAME AND PASSWORD
            Phone_number=username
            username_textbox= driver.find_element_by_id("email")
            username_textbox.send_keys(Phone_number)
            #------------------------------------------------------
            # SOLVE THE CAPTCHA

            a=driver.find_element_by_xpath("//*[@id=\"codeImg\"]/span[1]").text
            b=driver.find_element_by_xpath("//*[@id=\"codeImg\"]/span[2]").text
            c=driver.find_element_by_xpath("//*[@id=\"codeImg\"]/span[3]").text
            d=driver.find_element_by_xpath("//*[@id=\"codeImg\"]/span[4]").text
            my_string = "{}{}{}{}"
            e=my_string.format(a,b,c,d)
            username_textbox= driver.find_element_by_id("code")
            username_textbox.send_keys(e)
            x=driver.find_element_by_id("ok")
            x.click()
            time.sleep(6)
            
            # OPEN THE GMAIL
            progress.progress(q-60)
            driver.get('https://www.gmail.com/')
            time.sleep(10)
            # driver.find_element_by_class_name("y2").click()
            driver.find_element_by_class_name("y6").click()
            # driver.find_element_by_class_name("Zt").click()
            time.sleep(2)
            l=driver.find_element_by_partial_link_text("https://user.huami.com/")
            l.click()
            #--------------------------------------------------------------
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(5)
            element=driver.find_element_by_css_selector('body')
            time.sleep(1)
            progress.progress(q-50)
            element.send_keys(Keys.CONTROL+'a')
            time.sleep(1)
            element.send_keys(Keys.CONTROL+'c')
            time.sleep(1)
            password_user=pyperclip.paste()[55:63]
            st.write("Your Password for Zip file is: ")
            st.write(password_user)
            time.sleep(3)
            driver.find_element_by_id("download").click()
            time.sleep(5)
            progress.progress(q-40)
            st.write("Hurrah! Your data has been downloaded..")
            driver.close()
            import glob
            import os
            download_folder = os.path.expanduser("~")+"/Downloads/"
            download_folder=download_folder+'*'
            list_of_files = glob.glob(download_folder) 
            latest_file = max(list_of_files, key=os.path.getctime)
            latest_file=latest_file.replace('\\','\\\\\\\\')
            latest_file=latest_file.replace('/','\\\\\\\\')
            # st.write(latest_file) 
    
    if choice=="File selector to view data":
        import pandas as pd
        st.set_option('deprecation.showfileUploaderEncoding',False)
        st.title("VIEW YOUR DATA")
        uploaded_file=st.file_uploader(label="Upload your Csv or Excel file.",type=['csv','xlsx'])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)  
            st.write(df)
            
if __name__=="__main__":
    main()