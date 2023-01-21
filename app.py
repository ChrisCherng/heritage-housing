# Imports streamlit and multipage for the dashboard
import streamlit as st
from app_pages.multi_page import MultiPage

# Imports the dashboard pages from the app_pages folder
from app_pages.project_summary import project_summary_body
from app_pages.correlation_study import correlation_study_body
from app_pages.price_predictor import price_predictor_body
from app_pages.hypothesis import hypothesis_body
from app_pages.model_performance import model_performance_body

# Defines the multipage app
app = MultiPage(app_name="Heritage Housing")

# Sets the dashboard pages from the imported app_pages
app.app_page("Project Summary", project_summary_body)
app.app_page("House Sale Price Study", correlation_study_body)
app.app_page("House Sale Price Predictor", price_predictor_body)
app.app_page("Hypothesis and Validation", hypothesis_body)
app.app_page("ML Model Performance", model_performance_body)

# Runs the application
app.run()