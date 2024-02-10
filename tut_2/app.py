import streamlit as st
import json 
import pandas as pd 
import numpy as np 
import time as t 
import random
st.set_page_config(page_title="streamlit_tut_2")
st.header("Streamlit with Adarsh")
df = pd.DataFrame(np.random.randn(50,20),columns=["colm"+str(i) for i in range(20)] )
st.write(df)
# st.dataframe(df , width=700 , height = 500)
st.metric("Tata Motors",value=f"{900}", delta="3.98%")
price = st.empty()
prevprice,initialprice=189,189
for i in range(10):
    a = random.randint(0,5)
    if i%2==0:
        newprice = prevprice+a
    else:
        newprice=prevprice-a
    delta = round(((newprice-prevprice)/prevprice)*100,2)
    prevprice= newprice
    price.metric("IREDA",value=f"{newprice}", delta=f"{delta}%")
    t.sleep(1.5)