
from statistics import variance
import numpy as np
import pickle
import pandas as pd
import streamlit as st 
#from PIL import Image

#with open('style.css') as f:
   # st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


#app=Flask(__name__)
#Swagger(app)

pickle_in = open("air3.pkl","rb")
classifier=pickle.load(pickle_in)


def predict_note_authentication(Journey_day, Journey_month,Dep_hour,Dep_min,Airline_Air_Asia,Airline_Air_India):
       
    prediction=classifier.predict([[Journey_day, Journey_month,Dep_hour,Dep_min,Airline_Air_Asia,Airline_Air_India]])
    print(prediction)
    return prediction



def main():
    st.title("Mohit")
    html_temp = """
    <div style="background-color;padding:10px">
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)  

    Journey_day = st.text_input("Journey_day")
    Journey_month = st.text_input("Journey_month")
    Dep_hour = st.text_input("Dep_hour")
    Dep_min = st.text_input("Dep_min")
    Airline_Air_Asia = st.text_input("Airline_Air_Asia")    
    Airline_Air_India = st.text_input("Airline_Air_India")

   


    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Journey_day, Journey_month,Dep_hour, Dep_min,Airline_Air_India, Airline_Air_Asia)       

    if   (result == -0):  

        st.text('You MUST check')  
    st.success('Price of Journey {}'.format(result))
         

if __name__=='__main__':
    main()



