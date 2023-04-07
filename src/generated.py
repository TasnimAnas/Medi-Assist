import streamlit as st
# import openai
import json

class GeneratedDetails:
    def __init__(self) -> None:
        self.symptoms = []
        
    def gen(self):
        pass
        
    def app(self):
        st.title('Generated Details')
        st.subheader('Symptons Explanation')
        st.write('output comes here...')
        
        st.subheader('Possible Causes')
        st.write('output comes here')
        
        st.subheader('Tests')
        st.write('output comes here')