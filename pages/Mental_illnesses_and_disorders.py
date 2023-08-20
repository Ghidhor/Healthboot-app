import streamlit as st
import pandas as pd
import numpy as np

tableeee = pd.read_csv("table.xlsx")

#from streamlit_option_menu import option_menu

st.title("Health App")
st.markdown("## This is a list of some of the mental disorders affecting Teens")
st.markdown("##### This list only shows some of the symptoms , to know more , consult a psychiatrist or websites of medical organizations such as the CDC , WHO or the NHS")
st.table(tableeee)

st.markdown("## Do not actually use this app to figure out what mental disorder/illness you have , if you suspect that you have any , consult a Psychiatrist")


st.text("sources : Wikipedia , CDC , WHO , ACOG ,NHS , Psychiatry.org")

st.text("approved by godseeker yharim")
