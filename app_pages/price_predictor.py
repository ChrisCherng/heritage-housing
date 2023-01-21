# Import relevant libraries and data
import streamlit as st
import pandas as pd

from src.data_management import (load_house_prices_data, load_inherited_houses_data, load_pkl_file)
from src.machine_learning.predictive_analysis_ui import predict_price

# Body of information to be included in the dashboard
def price_predictor_body():
    st.write("### House Sale Price Predictor")

    st.info(
        f"The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa."
    )

    st.write("#### Inherited Properties")

    st.info(
        f"Information on the attributes of four houses inherited by the client are below. "
        f"Using the machine learning pipeline, the predicted sales price for each is listed below the table (referenced using the index in the table)."
    )    

    # Display the data for the inherited houses
    st.write(df_inherited_houses_data)

    st.write(
        f"* Index 0: 130,582\n"
        f"* Index 1: 154,283\n"
        f"* Index 2: 160,965\n"
        f"* Index 3: 181,734\n"
        f"* **Total: 627,564**\n"
    )

    st.write("#### Any Properties")

    st.info(
        f"The below can be used to input the key attributes of the house in Ames, Iowa, and output the predicted sales price."
    )

    # Add widgets to input attributes
    X_live = DrawInputsWidgets()

    price_prediction = predict_price(X_live, features, pipeline_regressor)

    if st.button("Predict Price"):
        st.success(f"Predicted house price: {price_prediction}")

# Load data, pipeline and features
version = 'v1'
df_inherited_houses_data = load_inherited_houses_data()
pipeline_regressor = load_pkl_file(f"outputs/ml_pipeline/predict_price/{version}/final_regressor_pipeline.pkl")
features = (pd.read_csv(f"outputs/ml_pipeline/predict_price/{version}/X_train.csv").columns.to_list())

# Function to create the input widgets for user predictions
def DrawInputsWidgets():

    # load dataset
    df = load_house_prices_data()
    percentageMin, percentageMax = 0.4, 2.0

    # create input widgets for the five best features
    col1, col2, col3 = st.beta_columns(3)
    col4, col5, col6 = st.beta_columns(3)

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # draw the widget based on the variable
    # and set initial values
    with col1:
        feature = "OverallQual"
        st_widget = st.number_input(
            label = feature,
            min_value = 1,
            max_value = 10,
            value = int(df[feature].median()),
            help = "Grading from 1 (Very Poor) to 10 (Very Excellent)"
        )
    X_live[feature] = st_widget

    with col2:
        feature = "GrLivArea"
        st_widget = st.number_input(
            label = feature,
            min_value = 0,
            max_value = 10000,
            value = int(df[feature].median()),
            help = "Above grade (ground) living area in whole square feet (max 10,000 sq feet)"
        )
    X_live[feature] = st_widget

    with col3:
        feature = "YearBuilt"
        st_widget = st.number_input(
            label = feature,
            min_value = 1820,
            max_value = 2023,
            value = int(df[feature].median()),
            help = "Original construction date (range from 1820 to 2023)"
        )
    X_live[feature] = st_widget

    with col4:
        feature = "GarageArea"
        st_widget = st.number_input(
            label = feature,
            min_value = 0,
            max_value = 1700,
            value = int(df[feature].median()),
            help = "Size of garage in whole square feet (max of 1,700 sq feet)"
        )
    X_live[feature] = st_widget

    with col5:
        feature = "1stFlrSF"
        st_widget = st.number_input(
            label = feature,
            min_value = 0,
            max_value = 5000,
            value = int(df[feature].median()),
            help = "First Floor area in whole square feet (max of 5,000 sq feet)"
        )
    X_live[feature] = st_widget

    return X_live