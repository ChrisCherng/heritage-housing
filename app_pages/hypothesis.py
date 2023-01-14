import streamlit as st

def hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect customers are churning with low tenure levels: Correct. The correlation study at Churned Customer Study supports that.\n"
        f"* A customer survey showed our customers appreciate fibre Optic. A churned user typically has Fibre Optic, as demonstrated by a Churned Customer Study. This insight will be used by the survey team for further discussions and investigations."
    )