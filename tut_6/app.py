import streamlit as st
import numpy as np
import datetime
from PIL import Image
from io import StringIO
from io import BytesIO
from PIL import UnidentifiedImageError
st.set_page_config(page_title="tut_6")
st.header("Streamlit with Adarsh")
text = st.text_area(
    label="Enter your text here ",
    height=200,
    max_chars=100,
    placeholder="Write here"
)
st.write(text)
bday = st.date_input(label="Enter your birthday ",
                     value=datetime.date(2024,2,11))
st.write(f"your birthday is on {bday}")
time = st.time_input(label="Enter your meal time ", value=datetime.time(14,00))
st.write(time)

files = st.file_uploader(label="Upload here",accept_multiple_files=True)
for file in files:
    if file :
        st.write(file.type)
        if "image" in file.type:
            img = Image.open(file)
            st.write(np.array(img).shape)
            st.image(img, caption="Uploaded Image", use_column_width=True)
        elif "text/plain" in file.type:
            stringio = StringIO(file.getvalue().decode("utf-8"))
            st.write(stringio.read())
pic = st.camera_input("Take a picture")
if pic:
    img = Image.open(BytesIO(pic.read()))
    st.image(img, caption="Your webcam selfie", use_column_width=True)
    buf = BytesIO()
    img.save(buf, format="JPEG")
    st.download_button(
      label="Download Image",
      data=buf.getvalue(),
      file_name="selfie.jpeg",
      mime="image/jpeg",
      )
color = st.color_picker("Pick a colour")
st.write(f"You selected {color}")




