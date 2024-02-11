import streamlit as st
import pandas as pd 
import numpy as np 
from datetime import time 
st.set_page_config(page_title="streamlit_tut_3")
st.header("Streamlit with Adarsh")
st.write("This is the multi select widget")
option = st.multiselect(
    label="Which places have you been ?",
    options=("Sydney","New Delhi","Bangkok","China","Nepal"),
    default=("New Delhi","Nepal")
)
st.write(option)

st.write("\n")
st.write("\n")
st.write("This is the slider widget")
num = st.slider(label="What is your age",
                min_value=18,
                max_value=100,
                value=20,
                step=1)
st.write(f"Your are {num} years old")
email = st.text_input(
    label="Email address",
    max_chars=50,
    placeholder="test@gmail.com",
)
password = st.text_input(
    label="password",
    placeholder="********",
    type="password"
)
st.write(f"{email} is your email id  and your password is {password}")

wt = st.number_input(
    label="Enter your weight",
    min_value=40,
    max_value=200,
    value=70,
    step=1
)