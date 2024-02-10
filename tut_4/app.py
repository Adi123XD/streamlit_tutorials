import streamlit as st
import pandas as pd 
import numpy as np 
import time
st.set_page_config(page_title="streamlit_tut_3")
st.header("Streamlit with Adarsh")
df = pd.DataFrame(np.random.randn(10,2),columns=["col_1","col_2"])
def fn ():
    st.write(time.time())
st.button("Click here",on_click=fn)
if (st.button("click here")):
    st.write(time.time())
    pass
data = df.to_csv().encode("utf-8")
st.download_button(label="Download file", data=data, file_name="random_file.csv" , mime="text/csv")

img = open(r"C:\Users\adars\Downloads\LearnIT_X.png", "rb")
st.download_button(label="Download image" , data=img , file_name="Learnit.png" , mime="image/png")
check = st.checkbox("Agree to the terms and conditions ?")
if (check):
    st.write("You Agreed to the terms and conditions")
else :
    st.write("Agree to the terms to use my website ")

option = st.radio(label="Order your food",
                  options=["Pizza","cold coffee","Chole Bhature"],
                  index=None)
if option=="Pizza":
    st.write("You ordered pizza")
elif option=="cold coffee":
    st.write("You ordered cold coffee")
elif option =="Chole Bhature":
    st.write("You ordered Chole Bhature")