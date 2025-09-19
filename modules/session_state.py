import streamlit as st

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "system", "content": "You are a helpful assistant."}]
    if "model_interactions" not in st.session_state:
        st.session_state["model_interactions"] = []
    if "selected_models" not in st.session_state:
        st.session_state["selected_models"] = ["deepseek-r1:1.5b", "qwen2:0.5b"]
    if "response_times" not in st.session_state:
        st.session_state["response_times"] = {}