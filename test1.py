import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np

st.title("Welcome to Mouma's  Rasoi")
st.subheader("----Fresh Home-Made Cakes and Chocolates----")
st.sidebar.title('ABOUT US:-')
st.sidebar.write("Mouma's Rasoi is widely known in kolkata for there innovations in making of a cake and chocolates.")
st.sidebar.markdown('Address: 12/3, Laketown BF-2, 3rd Lane, Kolkata-89')
st.sidebar.markdown("Website: www.moumasrasoi.com")
st.sidebar.markdown("Email: moumasrasoi@gmail.com")
st.sidebar.markdown("Contact: 9865321269")
image=Image.open("c8.jpg")
st.image(image,width=550,caption='Shape Your Emotions Into Cakes.')
st.subheader('Explore Our Fresh Cakes')
image=Image.open("c2.jpg")
st.image(image,width=250)
image=Image.open("c2.jpg")
st.image(image,width=250)
image=Image.open("c2.jpg")
st.image(image,width=250)
