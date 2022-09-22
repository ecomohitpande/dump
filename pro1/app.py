
from statistics import variance
import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
#from PIL import Image

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


#@app.route('/predict',methods=["Get"])
def predict_note_authentication(variance,skewness,curtosis,entropy):
    
       
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction



def main():
    st.title("Mohit")
    html_temp = """
    <div style="background-color;padding:10px">
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)


    variance = st.slider("variance", min_value=-8, max_value=6)
    skewness = st.text_input("skewness")
    curtosis = st.text_input("curtosis","Type Here")
    entropy = st.text_input("entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)       
    if  (result == -0):
            st.text('You MUST check')  
    st.success('output {}'.format(result))
         

if __name__=='__main__':
    main()



