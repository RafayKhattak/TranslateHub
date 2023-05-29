# Import necessary libraries and modules
import streamlit as st
from model import *

# Set page configuration and title for Streamlit
st.set_page_config(page_title="TranslateHub", page_icon="🔤", layout="wide")

# Add header with title and description
st.markdown(
    """
    <p style="display:inline-block;font-size:40px;font-weight:bold;">💬TranslateHub</p><br>
    <p style="display:inline-block;font-size:16px;">Harnessing pretrained models from Hugging Face, TranslateHub delivers impeccable language translation. <br><br></p>
    """,
    unsafe_allow_html=True
)

# Mapping of language choices to translation functions
language_map = {
    "English to Spanish": en_to_es,
    "English to French": en_to_fr,
    "English to German": en_to_de,
    "English to Chinese": en_to_zh,
    "English to Russian": en_to_ru,
    "English to Arabic": en_to_ar,
    "English to Japanese": en_to_ja,
    "English to Indonesian": en_to_id,
    "English to Urdu": en_to_ur,
    "English to Hindi": en_to_hi
}

# Language selection dropdown
languages = list(language_map.keys())
choice = st.selectbox("Select Language", languages)

# Translation process
text_area = st.text_area("Enter text", "")
if text_area is not None:
    if st.button("Translate"):
        col1, col2 = st.columns([1, 1])
        with col1:
            st.text("‎ ‎")
            st.info("Your Input Text:")
            st.success(text_area)
        with col2:
            st.text("This might even take a few mins.....")
            st.info("Your Translated Text:")
            translation_function = language_map.get(choice)
            result = translation_function(text_area)
            st.success(result)

# Hide Streamlit header, footer, and menu
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""

# Apply CSS code to hide header, footer, and menu
st.markdown(hide_st_style, unsafe_allow_html=True)
