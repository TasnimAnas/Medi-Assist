import json
import sys
from pathlib import Path

import streamlit as st

from src.routes import Routes

file_path = Path(__file__).parent / 'data/data.json'
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
