import streamlit as st

st.write("""
# Largest Number Finder App

This app finds the largest number
""")
#Get Input

st.header('User Input')

def user_input_features():
    num1 = st.number_input("FIRST NUMBER")
    num2 = st.number_input("SECOND NUMBER")
    num3 = st.number_input("THIRD NUMBER")

    data = {'FIRST NUMBER': num1,
            'SECOND NUMBER': num2,           
            'THIRD NUMBER': num3
            }
    return data

data = user_input_features() 


#Preprocessing

if (data['FIRST NUMBER'] == data['SECOND NUMBER']) & (data['SECOND NUMBER'] == data['THIRD NUMBER']):
    Keymax = 'None'
else:    
    Keymax = max(data, key= lambda x: data[x])



#Model Inferencing

st.subheader('Largest Number')
if Keymax == 'None':
    st.write(Keymax)    
else:
    st.write(Keymax,data[Keymax])
