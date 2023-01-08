import streamlit as st

def project_summary_body():
    st.write("### Project Summary")

    st.info(
        f"**Project Dataset**\n"
        f"* The dataset represents the housing records from Ames, Iowa, "
        f"indicating the profile of the house (e.g. Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) "
        f"and its respective sale price for houses built between 1872 and 2010.\n"
        f"* The data has been sourced from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data).\n\n"
        f"**Project Terms & Jargon**\n"
        f"* The **variables** are the different attributes of the house.\n"
        f"* The **target variable** is the variable that is trying to be predicted."
        f"For this project, this is the **sale price** of the house."
    )

    st.write(
        f"* For additional information, including full details of the data variables, please see the "
        f"[Project README file](https://github.com/ChrisCherng/heritage-housing)."
    )

    st.success(
        f"**Business Requirements**\n"
        f"* 1 - The client is interested in discovering how the house attributes correlate with the sale price. "
        f"Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.\n"
        f"* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa."
        )