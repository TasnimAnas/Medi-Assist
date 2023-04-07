import streamlit as st
from src.input import InputDetails
from src.generated import GeneratedDetails


class Routes:
    def __init__(self) -> None:
        self.model_name = None
        self.public_info = None
        self.assumptions = None
        self.assumptions_reasons = None

    def home(self) -> None:
        with open('./data/README.md') as f:
            home_text = f.read()
        st.markdown(home_text)

    def enter_data(self) -> None:
        InputDetails().app()
        
    def edit_data(self) -> None:
        gd = GeneratedDetails()
        gd.gen()
        gd.app()