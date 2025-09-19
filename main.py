import streamlit as st
from modules.styles import apply_custom_css
from modules.session_state import initialize_session_state
from modules.ui_components import render_sidebar, render_main_content
from modules.chat_utils import handle_user_input

# Page configuration
st.set_page_config(
    page_title="Ollama-Prism",
    page_icon="△",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
apply_custom_css()

# Initialize session state
initialize_session_state()

# Render UI components
render_sidebar()
render_main_content()

# Handle user input
handle_user_input()