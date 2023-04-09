import json
import os

import openai
import streamlit as st

openai.api_key = "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"

# print(req_lst)
f = open(r"C:\Users\KIIT\Desktop\medi-assist\data\data.json")
req_dict = json.load(f)
req_lst = req_dict["symptoms"]
possibleCause = ""


class GeneratedDetails:
    def __init__(self) -> None:
        self.symptoms = req_lst

    def gen(self):
        pass

    def app(self):
        st.title('Generated Details')
        # Taking a dummy list at first and then appending to it
        dummy_list = ["fever", "cough", "migraine"]
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


completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"What is the possible cause of {req_lst}? Just list the possible causes"}
    ]
)
possibleCause = completion.choices[0].message.content


# st.write('required output')
json.dumps(req_lst)

st.subheader('Possible Causes')
st.write(possibleCause)

st.subheader('Tests')
st.write('output comes here')
