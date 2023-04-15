import json
import sys
import uuid
from pathlib import Path

import streamlit as st

from src.routes import Routes

unique_id = str(uuid.uuid4())

if 'unique_id' not in st.session_state:
    st.session_state['unique_id'] = unique_id

st.set_page_config(page_title="Medi-Assist",
                   page_icon="https://raw.githubusercontent.com/shrutidebnath/medi-assist/main/medi-assist.ico")

pt = 'data/data_' + st.session_state['unique_id']+'.json'

file_path = Path(__file__).parent / pt
is_new_user = st.session_state.get('is_new_user', True)


def cleanup_json_file():
    with open(file_path, "w") as f:
        json.dump({"symptoms": []}, f)


# session_state = st.session_state.get(JSON_DATA_KEY, default={"symptoms": []})

def app() -> None:
    if is_new_user:
        cleanup_json_file()
        st.session_state['is_new_user'] = False

    rt = Routes()

    pages = {
        "Home": rt.home,
        "Enter Data": rt.enter_data,
        "Edit Details": rt.edit_data
    }

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", list(pages.keys()))
    pages[page]()

    # if st._is_running_with_streamlit:
    #     cleanup_json_file(session_state["data"])


if __name__ == "__main__":
    app()
    # app()
