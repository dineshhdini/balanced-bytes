import streamlit as st

# Sample LLM output data
llm_output = {
    "Ingredients": {
        "Potatoes": "Potatoes are the main ingredient in potato chips.",
        "Vegetable Oil": "Vegetable oil is used to fry the potato chips.",
        "Salt": "Salt is used to season the potato chips.",
        "Sugar": "Sugar is used to sweeten the potato chips.",
        # Add more ingredients as needed
    },
    "Nutritional Value": {
        "Energy": "537 kCal",
        "Protein": "5g",
        "Carbohydrates": "53g",
        # Add more nutritional values as needed
    },
    "Side Effects": {
        "Sugar": "Sugar can cause weight gain, tooth decay, and diabetes.",
        "Saturated Fat": "Saturated fat can increase cholesterol levels and heart disease risk.",
        # Add more side effects as needed
    }
}

# Define the sections
sections = list(llm_output.keys())

# Display the expanders for each section
for section_name in sections:
    with st.expander(section_name):
        section_data = llm_output[section_name]
        for idx, (key, value) in enumerate(section_data.items()):
            # Create a card for each ingredient with a unique key
            button_key = f"{section_name}_{idx}"  # Unique key for each button
            if st.button(key, key=button_key):
                # When the button is clicked, open a modal with the ingredient info
                st.write(value)
