import streamlit as st
st.title("This is my first web application in Python")
st.header("I'll try my best to learn Python for AI")
st.subheader("This is my first attempt to create a web app")
st.write("Hello everyone!") # basic print
st.text("Hello Prateek") # basic print
st.markdown("* Initial Assessment: A Healthy BMI")

if st.button('Press Now'):
    st.write('Hello Prateek!')

if st.checkbox('Show text'):
    st.write('This text is visible')

choice = st.radio("Pick one:", ["A", "B", "C"])
st.write(f"You picked {choice}")

option = st.selectbox("Choose an option", ["X", "Y", "Z"])
st.write(f"Option: {option}")

level = st.slider("Select a value", 1, 100)
st.write(f"Selected: {level}")

name = st.text_input("What's your name?")
st.write(f"Hello, {name}!")
age = st.number_input("What’s your age?")
st.write(f"Your age is: {age}")
