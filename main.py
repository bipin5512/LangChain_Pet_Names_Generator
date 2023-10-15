import langchain_helper as lch
import streamlit as st

st.title ("Pets Name Generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("Cat","Dog","Cow"))

if animal_type == 'Cat':
    pet_color = st.sidebar.text_area(label="What color is your Cat?", max_chars = 10)

if animal_type == 'Dog':
    pet_color = st.sidebar.text_area(label="What color is your Dog?", max_chars = 10)

if animal_type == 'Cow':
    pet_color = st.sidebar.text_area(label="What color is your Cow?", max_chars = 10)

if pet_color:
    response = lch.langchain_prompt_chain_pet_name_generator(animal_type=animal_type, pet_color=pet_color)
    st.text(response['pet_name'])

if animal_type and pet_color :
    st.sidebar.button("Submit")


#Command to run streamlit
#python -m streamlit run main.py