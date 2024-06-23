import streamlit as st
import pandas as pd

st.set_page_config(page_title="Diamond Analytics")
st.title('Glossary of Key Terms')

terms = pd.read_csv('key_terms.csv')

#make font sizes smaller
st.markdown("""
    <style>
    .small-font {
        font-size:12px !important;
    }
    </style>
    """, unsafe_allow_html=True)

for index, row in terms.iterrows():
    st.markdown(f"<h3 class='small-font'>{row['Term']}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p class='small-font'>{row['Definition']}</p>", unsafe_allow_html=True)

