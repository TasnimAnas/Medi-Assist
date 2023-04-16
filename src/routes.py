import streamlit as st

from src.generated import GeneratedDetails
from src.input import InputDetails


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
        st.markdown("_**1. Limited access to healthcare for people living in remote areas:** People living in remote areas may not have quick access to medical facilities and doctors. This can result in delayed diagnosis and treatment of health issues, which can have serious consequences for their health._")
        st.markdown("_**2. Avoidance of seeking medical attention due to lack of knowledge about symptoms:** Many people may avoid going to the doctor because they don't know the symptoms of potential health issues. This can lead to a worsening of their condition._")
        st.markdown("_**3. High costs associated with regular doctor visits:** For some people, the cost of regular doctor visits can be prohibitive. Which, people don't want to visit doctors which can make a medical condition worse and increase the likelihood of long-term health problems._")

        st.markdown('''
            <style>
            [data-testid="stMarkdownContainer"] ul{
                list-style-position: inside;
            }
            </style>
            ''', unsafe_allow_html=True)
        st.subheader("_Solutions_")
        st.markdown("Our app aims to solve the problem of limited access to healthcare for people living in remote areas by providing them with a convenient and cost-effective way to get an idea about their health issues. Using **OpenAI API**, the app empowers patients with knowledge and provides personalized healthcare recommendations based on the patient's age, height, weight, medical history, and current symptoms. The app also recommends which medical tests patients should undergo to confirm their diagnosis.\n\nThis platform can be used in any healthcare establishment and can be especially beneficial in remote places where people may have limited knowledge about certain medical conditions. The software can help reduce the time and cost of diagnosis, providing doctors and patients with a more efficient and effective healthcare solution. By leveraging OpenAI API, the app is able to provide very accurate and reliable recommendations, ensuring that patients receive the best possible advice for their specific needs. Our app is a required solution that helps to bridge the gap between patients and healthcare professionals, providing a valuable resource for people who may not have quick access to medical facilities or doctors.\n\nIt does not encourage patients to stop seeking medical attention and self diagnose but provides an outline of the condition that must only be treated through a physician's advice.")

    def enter_data(self) -> None:
        InputDetails().app()

    def edit_data(self) -> None:
        gd = GeneratedDetails()
        gd.gen()
        gd.app()
