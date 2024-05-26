import numpy as np
import pickle5 as pickle
import pandas as pd
import streamlit as st 

pickle_in = open("regression.pkl","rb")
regression=pickle.load(pickle_in)


pickle_x = open("scaler_x.pkl","rb")
loaded_scaler_x=pickle.load(pickle_x)

pickle_y = open("scaler_y.pkl","rb")
loaded_scaler_y=pickle.load(pickle_y)

def welcome():
    return "Welcome All"

def normalize_input(input_data):
    normalized_data = loaded_scaler_x.transform(input_data)
    return normalized_data

def inverse_transform(prediction):
    # Mengecek apakah prediksi memiliki bentuk 1D
    if prediction.ndim == 1:
        # Reshape prediksi menjadi array 2D dengan satu fitur
        prediction = prediction.reshape(-1, 1)
    inverse_prediction = loaded_scaler_y.inverse_transform(prediction)
    return inverse_prediction

def predict_compressive_strength(input_data):
    normalized_input = normalize_input(input_data)
    prediction=regression.predict(normalized_input)
    print(prediction)
    return prediction



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
    st.header("Enter the following details:")
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
        input_data = np.array([[Cement, Blast_Furnace, Fly_Ash, Water, Superplasticizer, Coarse_Aggregate, Fine_Aggregate, Age]])
        result = predict_compressive_strength(input_data)
        original_prediction = inverse_transform(result)
        st.success(f'Predicted Compressive Strength: {original_prediction[0][0]:.2f} MPa')
    
    # About section
    st.sidebar.markdown("### About")
    st.sidebar.info("This ML model predicts the compressive strength of concrete based on input features.")
    st.sidebar.caption("Copyright © 2024 Artificial Intelligence Class")


if __name__ == "__main__":
    main()
    
    
    