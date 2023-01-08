import streamlit as st
from src.data_management import load_house_prices_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

def correlation_study_body():

    df = load_house_prices_data()

    # hard copied from correlation study notebook
    vars_to_study = ['OverallQual', 'GrLivArea', 'GarageArea', 'YearBuilt', '1stFlrSF', 'TotalBsmtSF', 'KitchenQual']

    st.write("### House Sale Price Correlation Study")

    st.info(
        f"* The client is interested in discovering how the house attributes correlate with the sale price."
    )

    if st.checkbox("Inspect House Price Data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns. "
            f"Below are the first 10 rows of the data.")

        st.write(df.head(10))

    st.write("---")

    st.write(
        f"A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to the sales price. \n"
        f"Based on this study, the most correlated variable are: **{vars_to_study}**"
    )

    st.success(
        f"** Conclusions** \n"
        f"* Houses with higher overall quality score (i.e. higher quality material and finish) and quality of kitchen tend to have a higher sales price. \n"
        f"* Larger houses (i.e. with higher above ground living area, 1st floor area, basement area and (to a lesser extent) garage area) tend to sell for a higher price. \n"
        f"* Newer houses (i.e. those built more recently) will generally sell for a higher price, although the correlation is weaker than for the above attributes. \n"
    )

    st.write("---")

    st.info(
        f"* In addition, the client expects data visualisations of the correlated variables against the sale price."
    )

    st.write(
        f"Select the below to view scatterplots of the most correlated variables."
    )

    df_eda = df.filter(vars_to_study + ['SalePrice'])

    if st.checkbox("Sales Price per Variable"):
        sales_price_per_variable(df_eda)

    st.write("---")

    st.write(
        f"As part of the correlation study, heatmaps have been prepared to demonstrate the"
        f"correlation of variables to each other, as well as the Predictive Power Score (PPS)."
    )



def sales_price_per_variable(df_eda):
    """ Runs the scatterplots against SalePrice """
    target_var = 'SalePrice'
    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        plot_scatter(df_eda, col, target_var)
        print("\n\n")

def plot_scatter(df, col, target_var):
    """ Plots the scattergraphs against the target variable"""
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.scatterplot(data=df, x=col, y=target_var)
    plt.xticks(rotation=90)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)