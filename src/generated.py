import json
import os
from pathlib import Path

import openai
# import pyautogui
import streamlit as st

openai.api_key = "key"

# print(req_lst)


class GeneratedDetails:
    def __init__(self) -> None:
        pt = '../data/data_' + st.session_state['unique_id']+'.json'
        path = Path(__file__).parent / pt
        f = open(path)
        req_dict = json.load(f)
        self.req_lst = req_dict["symptoms"]
        self.age = req_dict["age"] if "age" in req_dict else 0
        self.gender = req_dict["gender"] if "gender" in req_dict else "Female"
        self.weight = req_dict["weight"] if "weight" in req_dict else 0
        self.height = req_dict["height"] if "height" in req_dict else 0
        self.med_history = req_dict["med_history"] if "med_history" in req_dict else "NA"
        causes = req_dict["causes"] if "causes" in req_dict else "No Data"
        tests = req_dict["tests"] if "tests" in req_dict else "No Data"
        # self.req_lst = self.req_lst
        self.causes = causes
        self.tests = tests

    def update_json(self, key, data):
        pt = '../data/data_' + st.session_state['unique_id']+'.json'
        path = Path(__file__).parent / pt
        with open(path, 'r') as f:
            self.inputJson = json.load(f)
        self.inputJson[key] = data
        with open(path, 'w') as f:
            json.dump(self.inputJson, f)

    def gen(self):
        pass

    def app(self):
        st.title('Generated Details')
        # Taking a dummy list at first and then appending to it
        # dummy_list = ["fever", "cough", "migraine"]
        list_size = len(self.req_lst)
        st.subheader('Symptoms Explanation')
        col1, col2 = st.columns(2)

        with col1:
            # symptom = st.text_area("Symptoms")
            for i in range(0, list_size):
                st.write(self.req_lst[i])
                i += 1

            symptom = st.text_area("Any other symptom you would like to add?")
            if st.button("Add"):
                st.success("Symptom added")
                # st.write(symptom)
                self.req_lst.append(symptom)
                if st.button("Delete Symptom"):
                    st.success("Symptom Deleted")
                    self.req_lst.remove(symptom)
                    print(self.req_lst)
                self.update_json("symptoms", self.req_lst)
                st.experimental_rerun()

        with col2:
            for i in range(0, list_size):
                # st.button("Delete Symptom", key=i)
                if st.button("Delete Symptom", key=i):
                    pt = '../data/data_' + \
                        st.session_state['unique_id']+'.json'
                    path = Path(__file__).parent / pt
                    with open(path, 'r') as f:
                        self.req_lst = json.load(f)["symptoms"]
                    st.success("Symptom Deleted")
                    self.req_lst.remove(symptom)
                    self.update_json("symptoms", self.req_lst)
                    st.experimental_rerun()
                i += 1

            # count1, count2 = 0, 0
        if st.button('Generate Report'):
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f" A {self.age} years old {self.gender} with a weight {self.weight} kg and height {self.height} cm is having {self.req_lst}. The patient has a medical history of {self.med_history}. What is the possible cause of these symptoms? Just list the possible causes"}
                ]
            )
            self.update_json(
                'causes', completion.choices[0].message.content)
            self.causes = completion.choices[0].message.content

            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f" A {self.age} years old {self.gender} with a weight {self.weight} kg and height {self.height} is having {self.req_lst}. The patient has a medical history of {self.med_history}. What medical diagnosis test should be suggested? Just list the possible tests"}
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

        # if st.button('Print Report'):
        #     pyautogui.hotkey('ctrl', 'p')
