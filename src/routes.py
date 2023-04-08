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
        st.markdown(""" <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style> """, unsafe_allow_html=True)

        st.title("**Medi-Assist**")
        """
        The code given below is mainly to condense the webpage such that the users do not have to do
        a lot of scrolling.
        """

        padding = 0
        st.markdown(f""" <style>
            .reportview-container .main .block-container{{
                padding-top: {padding}rem;
                padding-right: {padding}rem;
                padding-left: {padding}rem;
                padding-bottom: {padding}rem;
            }} </style> """, unsafe_allow_html=True)

        st.subheader("_Problem addressed_")
        st.markdown("_(i)Complex medical jargons which creates a communication gap between doctors and patients._")
        st.markdown("_(ii)Complex medical issues which some doctors might not be very familiar with, especially during their training years when they have less experience._")

        st.markdown('''
            <style>
            [data-testid="stMarkdownContainer"] ul{
                list-style-position: inside;
            }
            </style>
            ''', unsafe_allow_html=True)
        st.subheader("_Solutions_")
        st.markdown("_Our project aims to develop a platform or software that utilizes the BioGPT model by Microsoft to simplify complex medical jargon between patients and doctors. The software will allow doctors to enter the list of symptoms described by the patient, and then the BioGPT model will return a list of possible causes, diseases, medicines, tests, diet, etc. The doctor can edit this list to finalize the diagnosis. The data is then sent to the BioGPT model, which generates a detailed and easy-to-understand report in any language. The report will help patients to understand their diagnosis and treatment better. This platform can be used in any "
                    "healthcare establishment and can be especially beneficial in remote places where doctors may have limited knowledge about certain medical conditions. The software can help reduce the time and cost of diagnosis, providing doctors and patients with a more efficient and effective healthcare solution._")

    def enter_data(self) -> None:
        InputDetails().app()
        
    def edit_data(self) -> None:
        gd = GeneratedDetails()
        gd.gen()
        gd.app()
