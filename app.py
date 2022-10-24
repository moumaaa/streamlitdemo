import streamlit as st

st.title('this is a title')

st.write('i am mouma.......')

list=['wipro','ibm','deloitee','tcs']

x=st.radio('select your company', list)

st.write('i want to join', x)

y=st.number_input('enter a number', min_value=0, max_value=10,step=1)

st.write('the number is',y)