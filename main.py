import streamlit as st
from src.routes import Routes
import json

def app() -> None:
    rt = Routes()

    pages = {
        "Home": rt.home,
        "Enter Data": rt.enter_data,
        "Edit Details": rt.edit_data
    }

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", list(pages.keys()))
    pages[page]()

if __name__ == "__main__":
    app()