import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")
operation = st.selectbox("Choose Operation", ['Add', 'Subtract', 'Multiply', 'Divide'])

if st.button("Calculater"):
    if operation == 'Add':
        result = num1 + num2
    elif operation == 'Subtract':
        result = num1 - num2
    elif operation == 'Multiply':
            result = num1 * num2
    elif operation == 'Divide':
            result = num1 / num2 if num2 != 0 else 'Cannot divide by zero'
    st.success(f"Result: {result}")



# pip3 install streamlit                    # installs into your python3.12 (/usr/local/bin/python3)
# python3 -m streamlit run streamlit-calculator.py # or just: streamlit run streamlit-calculator.py
# pkill -f "streamlit run"

# cd /Volumes/work/kamal/python
# streamlit run streamlit-calculator.py
# pip3 install watchdog

#   You can now view your Streamlit app in your browser.

#   Local URL: http://localhost:8501
#   Network URL: http://192.168.x.x:8501
