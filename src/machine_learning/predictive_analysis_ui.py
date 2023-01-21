# Import streamlit library
import streamlit as st

# Run prediction from pipeline
def predict_price(X_live, features, pipeline):

    # from live data, subset features related to this pipeline
    X_live = X_live.filter(features)

    # predict
    price_prediction = int(pipeline.predict(X_live))

    return price_prediction