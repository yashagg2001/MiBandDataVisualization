import streamlit as st
import streamlit.components.v1 as components
def local_css(filename):
    with open(filename) as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)       
local_css('style.css')

components.html("<html><body><h1>VISUALIZATION OF YOUR FITNESS DATA</h1></body></html>")
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

if __name__=="__main__":
    main()