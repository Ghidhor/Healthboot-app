import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("Health App")
st.markdown("## This is an app for teen mental health")
st.markdown("#### Use the sidebar to navigate")

image = Image.open('mh.jpg')
st.image(image)
st.markdown("### :red[Why is Mental Health Important]")
st.text("Mental Health Affects our daily life , it decides how people think , feel  \nand behave. it dictates a person's interests , and their ability to make decisions \nMental health is important to everyone , not just a particular demographic \n \nIt is NOT something that is 'all in ones head' , or something that makes people \nweak or selfish. it is not an excuse for clout either    ")

st.text("approved by godseeker yharim")


