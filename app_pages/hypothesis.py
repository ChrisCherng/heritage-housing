import streamlit as st

def hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.info(
        f"In this project, it is hypothesised that larger and higher quality houses will have higher sales prices.\n"
    )

    st.success(
        f"* The correlation study shows that the variables OverallQual and GrLivArea have strong monotonic relationships with SalePrice - that is, a house with higher quality and larger living area tend to have higher sales price.\n"
        f"* In addition, the study shows that OverallQual and GrLivArea, along with 1stFlrSF have strong linear relationships with SalePrice.\n"
        f"* Therefore it can be concluded that houses that are larger and/or are of higher quality, generally have higher sales price.\n"
        f"* The hypothesis is deemed correct."
    )