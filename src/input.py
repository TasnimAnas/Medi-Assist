import streamlit as st
import json

class InputDetails:
    def __init__(self) -> None:
        self.symptoms = []
        self.name = None
        self.gender = None
        self.age = None
        self.weight = None
        self.inputJson = None
        
    def update_json(self, key, data):
        with open('data/data.json', 'r') as f:
            self.inputJson = json.load(f)
        self.inputJson[key] = data
        with open('data/data.json', 'w') as f:
            json.dump(self.inputJson, f)
        
    def app(self):
        st.title('Enter Details')
        
        st.subheader('Enter Patient History')
        col1, col2 = st.columns(2)
        with col1:
            self.name = st.text_input('Name')
            if self.name: self.update_json('name', self.name)
            self.gender = st.text_input('Gender')
            if self.gender: self.update_json('gender', self.gender)
        
        with col2:
            self.age = st.text_input('Age')
            if self.age: self.update_json('age', self.age)
            self.weight = st.text_input('Weight')
            if self.weight: self.update_json('weight', self.weight)
        
        self.med_history = st.text_input('Medical History')
        if self.med_history: self.update_json('med_history', self.med_history)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Enter Symptoms:")
            input = st.text_input('Enter Symptoms:', label_visibility='collapsed')
            if st.button('Add'):
                if input != "":
                    with open('data/data.json', 'r') as f:
                        self.symptoms = json.load(f)["symptoms"]
                    self.symptoms.append(input)
                    with open('data/data.json', 'w') as f:
                        json.dump({"symptoms": self.symptoms}, f)

        with col2:
            st.subheader("Symptoms List")
            with open('data/data.json', 'r') as f:
                self.symptoms = json.load(f)["symptoms"]
            for s in self.symptoms:
                st.text("> " + s)
            
            if len(self.symptoms) > 0:
                if st.button('Clear'):
                    with open('data/data.json', 'w') as f:
                        json.dump({"symptoms": []}, f)
                    st.experimental_rerun()