import streamlit as st
import pandas as pd
import numpy as np

st.title("Welcom ! contact us")
st.write("Complete  this form")

with st.form("my_form"):

    st.write("Personal Information")
    First_name = st.text_input("your first name")
    Last_Name = st.text_input("your mast name")
    Address=st.text_input("your Address")
    Phone=st.text_input("your phone Number ",max_chars=12)
    Email=st.text_input("your Email")
    photo=st.file_uploader("Upload a photo")
    description=st.text_area("Description:")
    st.write("Education")
    Degree = st.text_input("Your Degree ")
    Institution = st.text_input("Your Institution")
    Year=st.text_input("Your Graduation Year")
    st.write("Work experience")
    Position=st.text_input("Your Position")
    Company=st.text_input("Your Company")
    Duration=st.text_input("Your Duration")
    Responsibilities=st.text_input("Your Responsibilities")
    st.write("Skills")
    skills=st.text_input("add your skills")
    st.write("Language")