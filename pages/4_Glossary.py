import streamlit as st
import pandas as pd

st.set_page_config(page_title="Diamond Analytics")
st.title('Glossary of Key Terms')

terms = pd.read_csv('key_terms.csv')

for index, row in terms.iterrows():
    st.subheader(row['Term'])
    st.markdown(row['Definition'], unsafe_allow_html=True)

