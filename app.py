import streamlit as st
import os

st.title(":red[Innomatics] Data :blue[App] :sunglasses:")
st.snow()

btn_click = st.button("Don't click Me!")

if btn_click==True:
    st.subheader("You clicked the me :cry:")
    st.balloons()
    reset = st.button("Reset")





"""st.header("Data Science Internship")

st.subheader("Feb 2023")

CODE = '''print("Hello World")'''

st.code(CODE, language="python")"""