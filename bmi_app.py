import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "you are underweight."
    elif bmi < 25:
        return "you have a normal weight."
    elif bmi < 30:
        return "you are slightly overweight."
    elif bmi < 35:
        return "you are obese."
    else:
        return "you are clinically obese."

st.title("BMI Calculator")

height = st.number_input("Enter your height in metres:", min_value=0.0, format="%.2f")
weight = st.number_input("Enter your weight in kilograms:", min_value=0)

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        st.write(f"Your BMI is {bmi:.2f}, {category}")
    else:
        st.write("Please enter valid height and weight.")

st.write(f"Height: {height} metres")
