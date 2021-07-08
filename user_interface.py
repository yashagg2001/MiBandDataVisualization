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

            # RUN THE CHROME DRIVER AGAIN
            driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
            # ACCESSING THE EXTRACTING WEBSITE
            driver.get("http://online.b1.org/online")   
            time.sleep(4)
            x=driver.find_element_by_xpath("//*[@id=\"selectView\"]/form/div[2]/div/div/input").send_keys(latest_file)
            time.sleep(5)
            driver.find_element_by_xpath("//*[@id=\"passwordView\"]/div[2]/div/form/input[2]").send_keys(password_user)
            driver.find_element_by_xpath("//*[@id=\"passwordView\"]/div[2]/div/form/input[3]").click()
            time.sleep(5)
            driver.find_element_by_xpath("//*[@id=\"listView\"]/div[2]/table/tbody/tr[7]/td[1]/div/a").click() #heart_rate_auto
            driver.find_element_by_xpath("//*[@id=\"listView\"]/div[2]/table/tbody/tr/td[2]/a").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id=\"listView\"]/div[2]/div[1]/ul/li[2]/a").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id=\"listView\"]/div[2]/table/tbody/tr[1]/td[1]/div/a").click() #activity
            time.sleep(1)
            progress.progress(q-30)
            driver.find_element_by_xpath("//*[@id=\"listView\"]/div[2]/table/tbody/tr/td[2]/a").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id=\"listView\"]/div[2]/div[1]/ul/li[2]/a").click() 
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id=\"listView\"]/div[2]/table/tbody/tr[5]/td[1]/div/a").click()  #sleep
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id=\"listView\"]/div[2]/table/tbody/tr/td[2]/a").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id=\"listView\"]/div[2]/div[1]/ul/li[2]/a").click() 
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id=\"listView\"]/div[2]/table/tbody/tr[8]/td[1]/div").click() #user
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id=\"listView\"]/div[2]/table/tbody/tr/td[2]/a").click()
            time.sleep(3)
            progress.progress(q-0)
            
            driver.close()
            
            driver.quit()
            
            st.balloons()
            with st.spinner("You are almost ready"):
                time.sleep(4)
            st.success('Done!')
        
    #---------------------------------------------------------------------------------------------------------------
    # VISUALIZATION OF YOUR DATA
    if choice=="Visualize your data":
        import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np
        import warnings
        import datetime
        import matplotlib.dates as mdates
        warnings.filterwarnings("ignore")
        
        import glob
        import os
        import plotly.express as px
        from plotly.subplots import make_subplots
        import plotly.graph_objects as go
        for p in range(1,5):
            download_folder = os.path.expanduser("~")+"/Downloads/"
            download_folder=download_folder+'*'
            list_of_files = glob.glob(download_folder) # * means all if need specific format then *.csv
            latest_file = sorted(list_of_files, key=os.path.getctime)[-p]
            latest_file=latest_file.replace('\\','\\\\\\\\')
            latest_file=latest_file.replace('/','\\\\\\\\')
            # st.write(latest_file) 
            
            if(p==1):
                df_user=pd.read_csv(latest_file)
            elif(p==2):
                df_sl=pd.read_csv(latest_file)
                df_sl_copy=pd.read_csv(latest_file)
            elif(p==3):
                df_act=pd.read_csv(latest_file)
                df_act_copy=pd.read_csv(latest_file)
            else:
                df_hr=pd.read_csv(latest_file)
                df_hr_copy=pd.read_csv(latest_file)
        #--------------------
        user_name=df_user['nickName'][0]
        gender= df_user['gender']
        if(str(gender[0])=='1'):
            genderval='male'
        else:
            genderval='female'
        height=df_user['height']
        import streamlit.components.v1 as components
        # components.html("<html><body style='margin-top : -50px;'><h3>...Visualize your data...</h3></body></html>")
        st.markdown(f"<h2 style='text-align:center;color:white;background-color:black;margin-bottom:25px;padding-bottom:20px;margin-top:-40px;'>WELCOME {user_name}</h2>",unsafe_allow_html=True)
        # adding joeschmoe api for using avatar for the user
        st.markdown(f"<img src='https://joeschmoe.io/api/v1/{genderval}/{user_name}' class='centerit' width='200' height='200'>",unsafe_allow_html=True)
        st.markdown("***")
        latest_date_available=pd.to_datetime(df_hr_copy["date"].iloc[-1])
        start_date2 =pd.to_datetime(st.date_input('Pick a date for which you want to see your data', latest_date_available)).date()
        df_hr_copy['date']=pd.to_datetime(df_hr_copy['date']).dt.date
        df_sl_copy['date']=pd.to_datetime(df_sl_copy['date']).dt.date
        df_act_copy['date']=pd.to_datetime(df_act_copy['date']).dt.date
        df_hr_copy=df_hr_copy.loc[(df_hr_copy['date'] == start_date2)]
        df_act_copy=df_act_copy.loc[(df_act_copy['date'] == start_date2)]
        df_sl_copy=df_sl_copy.loc[(df_sl_copy['date'] == start_date2)]

        col1,col2=st.beta_columns(2)

        with col1:
            # TOTAL CALORIES BURNT ON SELECTED DATE
            document = (f'{df_act_copy["calories"].iloc[-1]} CAL')
            st.markdown(f'<div style="margin-top:0px;background-color:#00154f;height:150px; color:white; border-radius: 12px"><div style="background-color:#636EFA; padding:5px 5px 5px 5px; text-align:center;border-radius: 12px;">TOTAL CALORIES BURNT ON {str(start_date2)} :</div><h3 style="text-align:center; font-size:50px; margin-top:-10px;">🔥{document}</h3></div>',unsafe_allow_html=True)
            
        #-------------------
        with col2:
            # AVERAGE HEART RATE ON SELECTED DATE
            new_date=df_hr_copy['date'].iloc[-1]
            document1=(f"{round(np.mean((df_hr_copy[df_hr_copy['date']==new_date])['heartRate']))} BPM")
            st.markdown(f'<div style="margin-top:0px;background-color:#00154f; height:150px; color:white;border-radius: 12px;"><div style="background-color:#636EFA; padding:5px 5px 5px 5px; text-align:center;border-radius: 12px;">AVERAGE HEART RATE ON {str(start_date2)} :</div><h3 style="text-align:center; font-size:50px; margin-top:-10px;">💓{document1}</h3></div>',unsafe_allow_html=True)
        #------------------------------------
        #st.write(f'Total distance covered today: {(df_act["distance"].iloc[-1])/1000} KM')

        # TOTAL DISTANCE COVERED ON SELECTED DATE
        document2=(f'{(df_act_copy["distance"].iloc[-1])/1000} KM')
        st.markdown(f'<div style="margin-top: 30px; background-color:grey; height:150px; color:white;"><div style="background-color:black; padding:5px 5px 5px 5px; text-align:center;">TOTAL DISTANCE COVERED ON {str(start_date2)} :</div><h3 style="text-align:center; font-size:50px; margin-top:-10px;">👍{document2}</h3></div>',unsafe_allow_html=True)

        #---------------------------
        # TOTAL RUN DISTANCE COVERED ON SELECTED DATE 
        document3=(f'{(df_act_copy["runDistance"].iloc[-1])/1000} KM')
        st.markdown(f'<div style="margin-top: 30px;margin-bottom: 30px; background-color:#9DC88D; height:150px; color:white; "><div style="background-color:#4D774E; padding:5px 5px 5px 5px;text-align:center;">TOTAL RUN DISTANCE COVERED ON {str(start_date2)} :</div><h3 style="text-align:center; font-size:50px; margin-top:-10px;">🏃‍♂️{document3}</h3></div>',unsafe_allow_html=True)
        #------------------------------------------  
    
        #------------------------------------------
        #                                                   Steps related code
        st.markdown(f'<div><h2 style="color:#636EFA;text-align:center;"><b>YOUR TOTAL STEPS ON {str(start_date2)} IS :</b></h2></div>',unsafe_allow_html=True)
        todaydate= df_act_copy['date'].iloc[-1]
        todaysteps= df_act_copy['steps'].iloc[-1]
        document10= (f'{todaysteps}')
        a=st.text_input("Enter your steps goal here:",value="10000")
        per=f'{(int(todaysteps)*100)/int(a) }%'
        if(int(todaysteps)>int(a)):
            per=f'{100}%'
        st.markdown(f'<h2 style="margin-left:190px">Steps&emsp;&emsp;&emsp;&emsp;&ensp;Goal %</h2><div class="row d-flex justify-content-center mt-100"><div class="col-md-6"><div class="progress blue"> <span class="progress-left"> <span class="progress-bar"></span> </span> <span class="progress-right"> <span class="progress-bar"></span> </span><div class="progress-value">{document10}</div></div><div class="progress yellow"> <span class="progress-left"> <span class="progress-bar"></span> </span> <span class="progress-right"> <span class="progress-bar"></span> </span><div class="progress-value">{per}</div></div></div></div>',unsafe_allow_html=True)
        
        # -------------------------------------------
        # YOUR HEART VISUALIZATION ON SELECTED DATE
        import altair as alt
        df_hr_date=(df_hr_copy[df_hr_copy['date']==new_date])
        c2 = alt.Chart(df_hr_date).mark_line().encode(x="time", y="heartRate").configure_axisX(labelAngle=45)
        st.markdown(f'<div><h2 style="color:#e81a2b;text-align:center;"><b>💝&nbsp;YOUR HEART RATE VISUALIZATION ON <BR>{str(start_date2)} IS :</b></h2></div>',    unsafe_allow_html=True)
        st.altair_chart(c2)

        # YOUR WHOLE HEART VISUALIZATION
        c1 = alt.Chart(df_hr).mark_line().encode(x="time", y="heartRate").configure_axisX(labelAngle=45)
        st.markdown(f'<div><h2 style="color:#e81a2b;text-align:center;"><b>💝&nbsp;YOUR WHOLE HEART RATE VISUALIZTION</b></h2></div>',    unsafe_allow_html=True)
        st.altair_chart(c1)

        #-------------------------------------
        # PEAK DETECTION OF HEART RATE
        st.markdown(f'<div><h2 style="color:black;text-align:center;"><b>PEAK DETECTION OF YOUR HEART RATE<br> ON {str(start_date2)} :</b></h2></div>',    unsafe_allow_html=True)
        df_myhr=df_hr_copy.copy()
        from scipy.signal import find_peaks

        #defining the x and y arrays
        x = [i for i in range(len(df_myhr))]
        x=np.array(x)
        y = np.array(df_myhr['heartRate'])

        #Find peaks
        peaks = find_peaks(y, height = 1, threshold = 1, distance = 1)
        height = peaks[1]['peak_heights'] #list of the heights of the peaks
        peak_pos = x[peaks[0]] #list of the peaks positions

        #Finding the minima
        y2 = y*-1
        minima = find_peaks(y2)
        min_pos = x[minima[0]] #list of the minima positions
        min_height = y2[minima[0]] #list of the mirrored minima heights

        #Plotting
        fig = plt.figure()
        ax = fig.subplots()
        ax.plot(x,y)
        ax.scatter(peak_pos, height, color = 'r', s = 15, marker = 'D', label = 'Maxima')
        ax.scatter(min_pos, min_height*-1, color = 'gold', s = 15, marker = 'X', label = 'Minima')
        ax.legend()
        ax.grid()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

        # YOUR SLEEP DATA sELECTED DATE AND TODAY BY RADIO BUTTONS

        st.markdown(f'<div><h2 style="color:#636EFA;text-align:center;"><b>YOUR SLEEP DATA</b></h2></div>',unsafe_allow_html=True)
        list_names=["Not Selected",f"Your {str(start_date2)}'s sleep data","Your today's sleep data"]
        page=st.radio("Please select an option",list_names)
        if page=="Not Selected":
            st.warning("Select any option above...")
        elif(page=="Your today's sleep data"):
            s1,s2,s3=st.beta_columns(3)
            with s1:
                document4=(f'{(df_sl["deepSleepTime"].iloc[-1])//60} hrs and {(df_sl["deepSleepTime"].iloc[-1])-((df_sl["deepSleepTime"].iloc[-1])//60)*60} minutes')
                st.markdown(f'<div style="margin-top: 30px;margin-bottom: 30px; background-color:grey; height:150px; color:white;"><div style="background-color:black; padding:5px 5px 5px 5px;text-align:center;">Deep Sleep Time:</div><h3 style="text-align:center; font-size:30px; margin-top:-4px;">😴{document4}</h3></div>',unsafe_allow_html=True)

            with s2:
                document5=(f'{(df_sl["shallowSleepTime"].iloc[-1])//60} hrs and {(df_sl["shallowSleepTime"].iloc[-1])-((df_sl["shallowSleepTime"].iloc[-1])//60)*60} minutes')
                st.markdown(f'<div style="margin-top: 30px;margin-bottom: 30px; background-color:grey; height:150px; color:white; "><div style="background-color:black; padding:5px 5px 5px 5px; text-align:center;">Shallow Sleep Time:</div><h3 style="text-align:center; font-size:30px; margin-top:-4px;">⏱️{document5}</h3></div>',unsafe_allow_html=True)
            with s3:
                document6=(f'{(df_sl["wakeTime"].iloc[-1])//60} hrs and {(df_sl["wakeTime"].iloc[-1])-((df_sl["wakeTime"].iloc[-1])//60)*60} minutes')
                st.markdown(f'<div style="margin-top: 30px;margin-bottom: 30px; background-color:grey; height:150px; color:white; "><div style="background-color:black; padding:5px 5px 5px 5px; text-align:center;">Wake time:</div><h3 style="text-align:center; font-size:30px; margin-top:-4px;">💁‍♀️{document6}</h3></div>',unsafe_allow_html=True)
            
            # Your today Sleep Visualization
            st.markdown(f'<div><h2 style="color:#636EFA;text-align:center;"><b>YOUR TODAY\'S SLEEP VISUALIZATION</b></h2></div>',     unsafe_allow_html=True)
            ts=df_sl['deepSleepTime'].iloc[-1]+df_sl['shallowSleepTime'].iloc[-1]+df_sl['wakeTime'].iloc[-1]
            fig = px.pie(df_sl, values=[(df_sl['deepSleepTime'].iloc[-1]*100)/ts,(df_sl['shallowSleepTime'].iloc[-1]*100)/ts,(df_sl   ['wakeTime'].iloc[-1]*100)/ts], names=['Deep Sleep','Shallow Sleep', 'Wake Time'], title='Sleep Monitor')
            st.plotly_chart(fig)

        else:
            s1,s2,s3=st.beta_columns(3)
            with s1:
                document7=(f'{(df_sl_copy["deepSleepTime"].iloc[-1])//60} hrs and {(df_sl_copy["deepSleepTime"].iloc[-1])-((df_sl_copy["deepSleepTime"].iloc[-1])//60)*60} minutes')
                st.markdown(f'<div style="margin-top: 30px;margin-bottom: 30px; background-color:black; height:150px; color:white;"><div style="background-color:grey; padding:5px 5px 5px 5px;text-align:center;">Deep Sleep Time:</div><h3 style="text-align:center; font-size:30px; margin-top:-4px;">😴{document7}</h3></div>',unsafe_allow_html=True)

            with s2:
                document8=(f'{(df_sl_copy["shallowSleepTime"].iloc[-1])//60} hrs and {(df_sl_copy["shallowSleepTime"].iloc[-1])-((df_sl_copy["shallowSleepTime"].iloc[-1])//60)*60} minutes')
                st.markdown(f'<div style="margin-top: 30px;margin-bottom: 30px; background-color:black; height:150px; color:white; "><div style="background-color:grey; padding:5px 5px 5px 5px; text-align:center;">Shallow Sleep Time:</div><h3 style="text-align:center; font-size:30px; margin-top:-4px;">⏱️{document8}</h3></div>',unsafe_allow_html=True)
            with s3:
                document9=(f'{(df_sl_copy["wakeTime"].iloc[-1])//60} hrs and {(df_sl_copy["wakeTime"].iloc[-1])-((df_sl_copy["wakeTime"].iloc[-1])//60)*60} minutes')
                st.markdown(f'<div style="margin-top: 30px;margin-bottom: 30px; background-color:black; height:150px; color:white; "><div style="background-color:grey; padding:5px 5px 5px 5px; text-align:center;">Wake time:</div><h3 style="text-align:center; font-size:30px; margin-top:-4px;">💁‍♀️{document9}</h3></div>',unsafe_allow_html=True)
            
            # Your SELECTED DATE Sleep Visualization
            st.markdown(f'<div><h2 style="color:#636EFA;text-align:center;"><b>YOUR {str(start_date2)}\'S SLEEP VISUALIZATION</b></h2></div>',     unsafe_allow_html=True)
            ts=df_sl_copy['deepSleepTime'].iloc[-1]+df_sl_copy['shallowSleepTime'].iloc[-1]+df_sl_copy['wakeTime'].iloc[-1]
            fig = px.pie(df_sl_copy, values=[(df_sl_copy['deepSleepTime'].iloc[-1]*100)/ts,(df_sl_copy['shallowSleepTime'].iloc[-1]*100)/ts,(df_sl_copy['wakeTime'].iloc[-1]*100)/ts], names=['Deep Sleep','Shallow Sleep', 'Wake Time'], title='Sleep Monitor')
            st.plotly_chart(fig)

        #----------------------------------
        # ALL THREE BETA EXPANDERS
        
        with st.beta_expander("VISUALIZE YOUR CALORIES "):
            G1,G2=st.beta_columns(2)
            with G1:
                bars = alt.Chart(df_act).mark_bar().encode(x="calories", y="date")
                text = bars.mark_text(align='left', baseline='middle').encode( text='calories')
                (bars + text).properties(height=900)
                st.altair_chart(bars+text)
            with G2:
                cha3 = alt.Chart(df_act).mark_point().encode(x="distance", y="calories").configure_axisX(labelAngle=45)
                st.altair_chart(cha3)
        with st.beta_expander("VISUALIZE YOUR DATE VS DISTANCE"):
            cha = alt.Chart(df_act).mark_bar().encode(x="date", y="distance").configure_axisX(labelAngle=45)
            st.altair_chart(cha.properties(height=500,width=700))

        with st.beta_expander("VISUALIZE YOUR DATE VS DISTANCE"):
            cha2 = alt.Chart(df_act).mark_bar().encode(x="date", y="steps").configure_axisX(labelAngle=90)
            st.altair_chart(cha2)
        
        #------------------------------------
        # STATISTICAL ANALYSIS OF YOUR STEPS DISTANCE AND CALORIES
        st.markdown("***")
        st.markdown(f'<div><h2 style="color:GREY;text-align:center;"><b>STATISTICAL ANALYSIS</b></h2></div>',unsafe_allow_html=True)
        st.markdown("***")
        st.write(df_act[["steps", "distance","calories"]].describe())
        
        #----------------------------------------------------- 
        #heart rate prediction

        st.markdown("***")
        st.markdown(f'<div><h2 style="color:GREY;text-align:center;"><b>VISUALIZE YOUR HEARTRATE FOR A SELECTED RANGE</b></h2></div>',unsafe_allow_html=True)
        st.markdown("***")
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        start_date =pd.to_datetime(st.date_input('Start date', today)).date()
        end_date =pd.to_datetime(st.date_input('End date', tomorrow)).date()
        df_hr2=df_hr.copy()
        if start_date <= end_date:
            df_hr['time']=df_hr['date']+' '+df_hr['time']
            df_hr['date']=pd.to_datetime(df_hr['date']).dt.date
            mask = (df_hr['date'] >= start_date) & (df_hr['date'] <= end_date)
            df_hr = df_hr.loc[mask]
            st.markdown("***")
            st.write("Statistical analysis of your heart rate for the selected range")
            st.write(df_hr[["heartRate"]].describe())
            st.markdown("***")
            df_hr['time']=pd.to_datetime(df_hr['time'])
            df_hr.drop(['date'],axis='columns',inplace=True)
            st.write(df_hr)
        else:
            st.error('Error: End date must fall after start date.')
        

        # PLOTTING THE IMPORTANT FEATURES
        fig,ax=plt.subplots(figsize=(15,8))
        plt.plot(df_hr['time'],df_hr['heartRate'])
        xfmt=mdates.DateFormatter(' %d-%m-%y %H:%M')
        ax.xaxis.set_major_formatter(xfmt)
        plt.grid()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

        df_hr['heart_pct']=df_hr['heartRate'].pct_change().rolling(window=10).mean().values
        fig,ax=plt.subplots(figsize=(15,8))
        plt.plot(df_hr['time'],df_hr['heart_pct'])
        myfmt=mdates.DateFormatter('%H:%M')
        ax.xaxis.set_major_formatter(myfmt)
        plt.grid()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

        df_hr['heart_ma']=df_hr['heartRate'].rolling(window=500).mean().values
        fig,ax=plt.subplots(figsize=(16,8))
        plt.plot(df_hr['time'],df_hr['heartRate'],'-r',label='Heart Rate')
        plt.plot(df_hr['time'],df_hr['heart_ma'].rolling(window=500).mean().values,'c',label='DIFF')
        plt.legend()
        plt.grid()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

        fig,ax=plt.subplots(figsize=(16,8))
        plt.plot(df_hr['time'],df_hr['heartRate'],'-r',label='Heart Rate')
        plt.legend()
        plt.grid()
        ax.tick_params('x',colors='r')
        ax2=ax.twinx()
        plt.plot(df_hr['time'],df_hr['heart_ma'].rolling(window=1000).mean().values,'c',label='DIFF')
        plt.legend()
        ax2.tick_params('x',colors='b')
        myFmt=mdates.DateFormatter('%H:%M')
        ax2.xaxis.set_major_formatter(myFmt)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

        #-------------------------------------------------------------     

            
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