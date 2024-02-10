import streamlit as st
import pandas as pd 
import numpy as np 
st.set_page_config(page_title="streamlit_tut_3")
st.header("Streamlit with Adarsh")
df = pd.DataFrame(np.random.randn(10,2),columns=["col_1","col_2"])
st.write("plotting charts in streamlit")
st.line_chart(df)
st.line_chart(df, y="col_1")
st.area_chart(df)
st.bar_chart(df)
st.map()
