import streamlit as st

st.write("""
# Largest Number Finder App

This app finds the largest among 3 given numbers (value greater than the other two)
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

lk, lv = list(data.keys()),list(data.values())
maxv = max(lv)
count=0

for i in lv:
  if i==maxv:
    count+=1
    
if count>1:
    maxval = 'None'
else:    
    maxval = maxv



#Model Inferencing

st.subheader('Largest Number')
if maxval == 'None':
    st.write(maxval)    
else:
    Keymax = lk[lv.index(maxval)]
    st.write(Keymax,maxval)
