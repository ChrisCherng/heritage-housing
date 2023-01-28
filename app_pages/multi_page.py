# Import streamlit
import streamlit as st

# Setup streamlit multipage
class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title = self.app_name,
        )

    def app_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})
    
    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()