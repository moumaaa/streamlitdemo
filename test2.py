import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np

image=Image.open('iem nav.png')
st.image(image,width=730)
st.sidebar.title('ABOUT:')
st.sidebar.subheader('IEM is a local private enginering and management college located in kolkta, west bengal,India. It is private enginering college in west bengal. it is affialiated to MAKAUT. It was established in 1989.')
st.sidebar.write('Address: 34/2, BE Block,Sector V, Biddhannagar, Kolkata,West Bengal 700091')
st.sidebar.write('Email: admissions@iemcal.com')
st.sidebar.write('Website: iem.edu.in')
st.sidebar.write('Contact: 8010700500')
st.subheader('-----------------------------Admission Form----------------------------')
st.text('Enter your admission information Below:')
name = st.text_input("Enter Your name: ")

if(st.button('Done')):
    result = name.title()
    st.success(result)
list=['Male','Female']
status = st.radio("Gender: ", list)
 
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")

y=st.text_input('Birth Date: ')

st.write('Your Birth Date is: ',y)
name = st.text_input("Phone no: ")
name = st.text_input("Email Id: ","xyz@gmail.com")
name = st.text_input("Enter Your mother's name: ")
name = st.text_input("Enter Your father's name: ")

name = st.text_input("School Name: ")
y=st.number_input('Last Examination marks in(%)', min_value=30, max_value=100,step=1)

st.write('Secured Marks is',y)
course = st.selectbox("Select Your Course: ",
                     ['B.Tech', 'BCA', 'BBA','MCA','MBA','M.Tech'])
 
st.write("Your selected course is: ", course)

hobbies = st.multiselect("Hobbies: ",
                         ['Dancing', 'Singing', 'Sports','Reading','Others'])
 
st.write("You selected", len(hobbies), 'hobbies')

name = st.text_input("Your Address: ")
state= st.selectbox("State: ",
                     ['Andhra Pradesh','Amaravati','Arunachal Pradesh',	'Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana',	
                     'Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram'	
                     'Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'])
 
st.write("State: ", state)

if(st.button("NEXT")):
    st.text('Check your email regurlarly for further updates')

st.subheader('Why IEM?')
image=Image.open('iem logo.png')
st.image(image,width=400,caption='Good Education,Good Job')
st.write('IEM can proudly state that every year students of the institute perform brilliantly in the MAKAUT semester examination and several students are declared as University toppers.'
'Ranked 101th All India by NIRF(2019).All eligible departments are NBA accredited(CSE,IT,ECE)'
'Approximately 100% placement of engineering and management students. Many of them grab multiple job offers.')


l = st.slider("Give your rating", 1, 5)
if(l==5):
    st.success('Thanks for your valuable rating')  

if st.checkbox("Re-check your form before submitting"):
 
    st.text("That's Great!")
else:
    st.error('This field is required')


if(st.button("Sumbit")):
    st.text('Thank you for submitting. '
    'Your response has been recorded!!!')