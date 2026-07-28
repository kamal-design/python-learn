# app.py
import streamlit as st

st.title("My first streamlit app")
st.header("Welcome to the demo app")
st.write("This is a simple app built with streamlit!")

# Interactive element
name = st.text_input("What's your name?")
if name:
    st.success(f"Hello, {name}! 👋")

# Slider example
age = st.slider("Select your age", 1, 100, 25)
st.write("You selected:", age)


# pip3 install streamlit                    # installs into your python3.12 (/usr/local/bin/python3)
# python3 -m streamlit run streamlit_app.py # or just: streamlit run streamlit_app.py
# pkill -f "streamlit run"

# cd /Volumes/work/kamal/python
# streamlit run streamlit_app.py
# pip3 install watchdog

#   You can now view your Streamlit app in your browser.

#   Local URL: http://localhost:8501
#   Network URL: http://192.168.x.x:8501
