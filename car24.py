import streamlit as st 
import pandas as pd
import pickle 

st.title("Car price prediction app")

#Fuel Type, Transmission Type, engine power, seats
col1, col2 =st.columns(2)

with col1:
    fuel_type = st.radio('Fuel Type', ['Petrol', 'Diesel', 'LPG', 'Electric'])
    
with col2:
    transmission_type=st.selectbox('Transmission Type', ['Manual', 'Automatic'])
    
col3, col4 = st.columns(2)
with col3:
    engine_power= st.slider('Engine Power', 500, 5000, step=100)

with col4:
    seats= st.selectbox('Seats', [2,4,5,6,7,8,9,10])
    
model = pickle.load(open("car24.ipynb", "rb"))

encode_dict={
    'fuel_type': {'Diesel' :1, 'Electric': 2, 'LPG':3,'Petrol' : 4}}
    #'transmission_type' :{'Manual': 1, 'Automatic':2}}

def model_pred(fuel_type, temperature_type, engine_power, seats):

    fuel_type=encode_dict(fuel_type=encode_dict['fuel_type'][fuel_type] )                                # 'transmission_type'][transmission_type]

    
    data=[[2018.8, 1, 40000, fuel_type, transmission_type, 18.0, engine_power, 85, seats]]
    return round(model.predict(data)[0],2)

if st.button('Predict'):
    st.write(model_pred(fuel_type, transmission_type, engine_power, seats))
    
else:
    st.write('Please done with data')