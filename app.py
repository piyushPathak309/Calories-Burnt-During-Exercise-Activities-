import streamlit as st
import pickle


model = pickle.load(open('Calbuntrfmodel.pkl', 'rb'))

st.title("Calories Burnt During Exercise/Activities")

Gender = str(st.selectbox('Gender', ['male', 'female']))
if Gender=='male':
    Gender=0
else:
    Gender=1
Age = st.text_input("Age")
Weight = st.text_input("Weight")
Duration = st.text_input("Duration")
if st.button("Predict Calories"):
    query = model.predict([[Gender,Age, Weight,Duration]])
    output = round(query[0],4)
    st.success(f'Calories Burnt(Per Kg) {output}')






































































