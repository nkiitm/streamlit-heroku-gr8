import streamlit as st
import pandas as pd

st.write("""
# Largest Number Finder App

This app finds the largest number
""")
#Get Input

st.header('User Input')

def user_input_features():
    num1 = st.number_input("FIRST NUMBER",min_value=-20000,max_value=400000 ,step=1)
    num2 = st.number_input("SECOND NUMBER",min_value=-20000,max_value=400000 ,step=1)
    num3 = st.number_input("THIRD NUMBER",min_value=-20000,max_value=400000 ,step=1)

    data = {'FIRST NUMBER': num1,
            'SECOND NUMBER': num2,           
            'THIRD NUMBER': num3
            }
    return data

data = user_input_features() 
df = pd.DataFrame(data, index=[0])

st.subheader('User Input')
st.write(df.to_dict())


#Preprocessing

Keymax = max(data, key= lambda x: data[x])



#Model Inferencing

st.subheader('Largest Number')
st.write(Keymax)
