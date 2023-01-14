import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from src.data_management import load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_price
from src.machine_learning.evaluate_pipeline import regression_performance, regression_evaluation, regression_evaluation_plots

def model_performance_body():

    # load pipeline files
    version = 'v1'
    predict_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_price/{version}/final_regressor_pipeline.pkl")
    feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_price/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{version}/y_train.csv")
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{version}/y_test.csv")

    st.write("### ML Model Performance")

    st.info(
        f"* A regressor model was built to predict the sales price of houses in Ames, Iowa, to address the second business requirement.\n"
        f"* The client required the model have an R2 score of at least 0.7.\n"
        f"* Both the train set and test set achieved R2 scores in excess of the requirement, at 0.839 and 0.773.\n"
        f"* Therefore the model has been deemed suitable to meeting the client's needs.\n"
        f"* The sections below detail more information about the pipeline model and its associated performance metrics."
        )

    st.write("---")

    # show pipeline steps
    st.write("The ML pipeline that has been developed to predict the sale price of houses in Ames, Iowa, is as follows:")
    st.write(predict_price_pipe)

    st.write("---")

    # show best features
    st.write("The features the model was trained on, and their importance, are shown below.")
    st.write(X_train.columns.to_list())
    st.image(feat_importance)

    st.write("---")

    # evaluate performance on both sets
    st.write("### Pipeline Performance")

    st.write("The key metrics evaluating the performance of the pipeline are shown below.")

    regression_performance(X_train, y_train, X_test, y_test, predict_price_pipe)

    st.write("The predicted sale price values have been compared to the actual values in the plots below.")

    regression_evaluation_plots(X_train, y_train, X_test, y_test, predict_price_pipe)