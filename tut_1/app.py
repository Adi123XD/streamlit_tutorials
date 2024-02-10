import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
st.header("Streamlit with Adarsh ")
st.text("This is a default text ")
st.write("This is **just** a _**text**_")

# how to read and display a csv file in streamlit 
st.write("how to read and display a csv file in streamlit ")
df = pd.read_excel(r"C:\Users\adars\Downloads\Copy of Manipal_University_Jaipur(1).xlsx")
st.write(df)

# plots in streamlit 
st.write("plots in streamlit ")
plt.figure(figsize=(7,7))
fig,ax = plt.subplots(1,2)
ax[0].scatter(np.arange(5),np.arange(5)**2)
ax[1].scatter(np.arange(5),np.arange(5)**3)
st.pyplot(fig)


# how to display a python code in streamlit 
st.write("how to display a python code in streamlit")
code ="""plt.figure(figsize=(7,7))
fig,ax = plt.subplots(1,2)
ax[0].scatter(np.arange(5),np.arange(5)**2)
ax[1].scatter(np.arange(5),np.arange(5)**3)
st.pyplot(fig)"""
st.code(code,language="python")



