import streamlit as st



# Title of the app
st.title("🌏 Unit Converter App")

st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
        font-family: Arial, sans-serif;
    }
    .stTitle {
        color: #ff6600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Subtitle of the app
st.markdown("### Converts Length, Weight, And Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

# Select category (Length, Weight, Time)
category = st.selectbox("Select Category", ["Length", "Weight", "Time"])

# Conversion logic
def convert_units(category, value, unit):
    if category == "Length":
        conversions = {
            "Kilometers to Miles": value * 0.621371,
            "Miles to Kilometers": value / 0.621371,
        }
    elif category == "Weight":
        conversions = {
            "Kilograms to Pounds": value * 2.20462,
            "Pounds to Kilograms": value / 2.20462,
        }
    elif category == "Time":
        conversions = {
            "Seconds to Minutes": value / 60,
            "Minutes to Seconds": value * 60,
            "Minutes to Hours": value / 60,
            "Hours to Minutes": value * 60,
            "Hours to Days": value / 24,
            "Days to Hours": value * 24,
        }
    else:
        return None  # Return None if the category is invalid

    return conversions.get(unit, None)  # Return None if unit not found

# Unit selection
if category == "Length":
    unit = st.selectbox("🔗 Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("🔗 Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("🔗 Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

# User input value
value = st.number_input("Enter value to convert:", min_value=0.0)

# Convert button
if st.button("Convert"):
    result = convert_units(category, value, unit)
    
    if result is not None:  # Check if conversion was successful
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Invalid conversion. Please check your input.")