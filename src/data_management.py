# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import joblib


# Create dataframe with house price data
@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_house_prices_data():
    df = pd.read_csv("outputs/datasets/collection/HousePricesRecords.csv")
    return df

# Create dataframe with inherited houses data
@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_inherited_houses_data():
    df = pd.read_csv("inputs/datasets/raw/house-price-20211124T154130Z-001/house-price/inherited_houses.csv")
    return df

# Load PKL file
def load_pkl_file(file_path):
    return joblib.load(filename=file_path)