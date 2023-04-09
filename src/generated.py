import json
import os

import openai
import streamlit as st

openai.api_key = "key"

# print(req_lst)


class GeneratedDetails:
    def __init__(self) -> None:
        f = open(r"C:\Users\KIIT\medi-assist\data\data.json")
        req_dict = json.load(f)
        req_lst = req_dict["symptoms"]
        self.age = req_dict["age"]
        self.gender = req_dict["gender"]
        self.weight = req_dict["weight"]
        self.med_history = req_dict["med_history"]
        causes = req_dict["causes"] if "causes" in req_dict else "No Data"
        tests = req_dict["tests"] if "tests" in req_dict else "No Data"
        self.symptoms = req_lst
        self.causes = causes
        self.tests = tests

    def update_json(self, key, data):
        with open('data/data.json', 'r') as f:
            self.inputJson = json.load(f)
        self.inputJson[key] = data
        with open('data/data.json', 'w') as f:
            json.dump(self.inputJson, f)

    def gen(self):
        pass

    def app(self):
        st.title('Generated Details')
        # Taking a dummy list at first and then appending to it
        # dummy_list = ["fever", "cough", "migraine"]
        list_size = len(self.symptoms)
        st.subheader('Symptoms Explanation')
        col1, col2 = st.columns(2)

        with col1:
            # symptom = st.text_area("Symptoms")
            for i in range(0, list_size):
                st.write(self.symptoms[i])
                i += 1

            symptom = st.text_area("Any other symptom you would like to add?")

        with col2:
            for i in range(0, list_size):
                # st.button("Delete Symptom", key=i)
                if st.button("Delete Symptom", key=i):
                    st.success("Symptom Deleted")
                    req_lst.remove(symptom)
                i += 1

            # count1, count2 = 0, 0
            if st.button("Add"):
                st.success("Symptom added")
                with col1:
                    st.write(symptom)
                    req_lst.append(symptom)
                if st.button("Delete Symptom"):
                    st.success("Symptom Deleted")
                    req_lst.remove(symptom)
        if st.button('Generate Report'):
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f" A {self.age} years old {self.gender} with a weight {self.weight} is having {self.symptoms}. The patient has a medical history of {self.med_history}. What is the possible cause of these symptoms? Just list the possible causes"}
                ]
            )
            self.update_json(
                'causes', completion.choices[0].message.content)
            self.causes = completion.choices[0].message.content

            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f" A {self.age} years old {self.gender} with a weight {self.weight} is having {self.symptoms}. The patient has a medical history of {self.med_history}. What medical diagnosis test should be suggested? Just list the possible tests"}
                ]
            )
            self.update_json(
                'tests', completion.choices[0].message.content)
            self.tests = completion.choices[0].message.content

        # st.write('required output')
        # json.dumps(req_lst)
        # json.dumps(causes)
        # json.dumps(tests)

        st.subheader('Possible Causes')
        st.write(self.causes)

        st.subheader('Tests')
        st.write(self.tests)
