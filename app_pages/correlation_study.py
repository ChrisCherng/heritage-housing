# Import relevant libraries and data
import streamlit as st
from src.data_management import load_house_prices_data

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
import ppscore as pps

# Body of information to be included in the dashboard
def correlation_study_body():

    # Set dataframe with house price data
    df = load_house_prices_data()

    # hard copied from correlation study notebook
    vars_to_study = ['OverallQual', 'GrLivArea', 'GarageArea', 'YearBuilt', '1stFlrSF', 'TotalBsmtSF', 'KitchenQual']

    st.write("### House Sale Price Correlation Study")

    st.info(
        f"* The client is interested in discovering how the house attributes correlate with the sale price."
    )

    # Checkbox widget for displaying data
    if st.checkbox("Inspect House Price Data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns. "
            f"Below are the first 10 rows of the data.")

        st.write(df.head(10))

    st.write("---")

    st.write(
        f"A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to the sales price. \n"
        f"Based on this study, the most correlated variables are: **{vars_to_study}**"
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
        f"Select the below to view scatterplots of the most correlated variables. "
        f"This shows how each of the selected variables compares to the target variable of SalePrice. "
        f"The correlations can be seen through the patterns in the scatterpoints, showing the trends."
    )

    # Set dataframe filtered for only variables to study
    df_eda = df.filter(vars_to_study + ['SalePrice'])

    if st.checkbox("Sales Price per Variable"):
        sales_price_per_variable(df_eda)

    st.write("---")

    st.write(
        f"As part of the correlation study, heatmaps have been prepared to demonstrate the "
        f"correlation of variables to each other, as well as the Predictive Power Score (PPS)."
    )

    # Checkbox widget to display the Spearman correlation information
    if st.checkbox("Spearman Correlations"):
        st.write(
            f"* This plot shows how correlated each variable is to each other, in terms of a monotonic relationship.\n"
            f"* Only those with a score over 0.6 are displayed, to show the strong correlations."
            )
        df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)
        heatmap_corr(df=df_corr_spearman, threshold=0.6, figsize=(20, 12), font_annot=15)

    # Checkbox widget to display the Pearson correlation information
    if st.checkbox("Peason Correlations"):
        st.write(
            f"* This plot shows how correlated each variable is to each other, in terms of a linear relationship.\n"
            f"* Only those with a score over 0.6 are displayed, to show the strong correlations."
            )
        df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)
        heatmap_corr(df=df_corr_pearson, threshold=0.6, figsize=(20, 12), font_annot=15)

    # Checkbox widget to display the PPS information
    if st.checkbox("Predictive Power Score"):
        st.write(
            f"* This plot shows how strong a variable (on the x-axis) can predict a variable on the y-axis.\n"
            f"* Only those with a score over 0.15 are displayed, to show the strong predictive powers."
            )
        df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)
        heatmap_pps(df=pps_matrix, threshold=0.15, figsize=(20, 12), font_annot=15)

# Functions to display scatterplots to show correlations
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


# Functions to display heatmaps for correlation and PPS
def heatmap_corr(df, threshold, figsize=(20, 12), font_annot=15):
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True
        mask[abs(df) < threshold] = True

        fig, axes = plt.subplots(figsize=figsize)
        sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                    mask=mask, cmap='viridis', annot_kws={"size": font_annot}, ax=axes,
                    linewidth=0.5
                    )
        axes.set_yticklabels(df.columns, rotation=0, fontsize=20)
        axes.set_xticklabels(df.columns, fontsize=20)
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)


def heatmap_pps(df, threshold, figsize=(20, 12), font_annot=15):
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=np.bool)
        mask[abs(df) < threshold] = True
        fig, ax = plt.subplots(figsize=figsize)
        ax = sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                         mask=mask, cmap='rocket_r', annot_kws={"size": font_annot},
                         linewidth=0.05, linecolor='grey')
        ax.set_yticklabels(df.columns, rotation=0, fontsize=20)
        ax.set_xticklabels(df.columns, fontsize=20)
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)

# Function to calculate correlations and PPS
def CalculateCorrAndPPS(df):
    df_corr_spearman = df.corr(method="spearman")
    df_corr_pearson = df.corr(method="pearson")

    pps_matrix_raw = pps.matrix(df)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(columns='x', index='y', values='ppscore')

    return df_corr_pearson, df_corr_spearman, pps_matrix