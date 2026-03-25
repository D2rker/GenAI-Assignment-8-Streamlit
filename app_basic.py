import streamlit as st

st.title("Welcome to Streamlit!")

user_name = st.text_input("Enter your name:")

if st.button("Greet Me"):
        st.write("Hello, !")
