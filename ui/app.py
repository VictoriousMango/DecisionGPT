import streamlit as st

st.title("DesicionGPT")

query = st.text_input("Ask you queries:")

if query:
    st.write(query)