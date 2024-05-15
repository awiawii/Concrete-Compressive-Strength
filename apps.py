import numpy as np
import pickle
import pandas as pd
import streamlit as st 

pickle_in = open("regression.pkl","rb")
regression=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_compressive_strength(Cement,Blast_Furnace,Fly_Ash,Water,Superplasticizer,Coarse_Aggregate,Fine_Aggregate,Age):
   
    prediction=regression.predict([[Cement,Blast_Furnace,Fly_Ash,Water,Superplasticizer,Coarse_Aggregate,Fine_Aggregate,Age]])
    print(prediction)
    return prediction



import streamlit as st

def main():
    st.title("Concrete Compressive Strength Prediction")
    
    # HTML template for header
    html_temp = """
    <div style="background-color:#007bff;padding:10px;border-radius:10px">
    <h2 style="color:white;text-align:center;">ML Prediction App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Input fields
    st.subheader("Enter the following details:")
    Cement = st.text_input("Cement (kg/m³)")
    Blast_Furnace = st.text_input("Blast Furnace Slag (kg/m³)")
    Fly_Ash = st.text_input("Fly Ash (kg/m³)")
    Water = st.text_input("Water (kg/m³)")
    Superplasticizer = st.text_input("Superplasticizer (kg/m³)")
    Coarse_Aggregate = st.text_input("Coarse Aggregate (kg/m³)")
    Fine_Aggregate = st.text_input("Fine Aggregate (kg/m³)")
    Age = st.text_input("Age (days)")
    
    # Prediction and output
    result = ""
    if st.button("Predict"):
        result = predict_compressive_strength(Cement, Blast_Furnace, Fly_Ash, Water, Superplasticizer, Coarse_Aggregate, Fine_Aggregate, Age)
    st.success('Predicted Compressive Strength: {} MPa'.format(result))
    
    # About section
    st.sidebar.markdown("### About")
    st.sidebar.info("This ML model predicts the compressive strength of concrete based on input features.")
    st.sidebar.caption("Copyright © 2024 Artificial Intelligence Class")

def predict_compressive_strength(Cement, Blast_Furnace, Fly_Ash, Water, Superplasticizer, Coarse_Aggregate, Fine_Aggregate, Age):
    # Your prediction function implementation goes here
    pass

if __name__ == "__main__":
    main()
    
    
    