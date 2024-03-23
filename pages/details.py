# import streamlit as st
# from flask import Flask, redirect, url_for
# import requests
# # from streamlit_lottie import st_lottie

# def main():
#     st.set_page_config(initial_sidebar_state="collapsed", page_title="Balanced Bytes - check your diet",page_icon='🌱', layout="wide")
#     st.markdown(
#     """
# <style>
#     [data-testid="collapsedControl"] {
#         display: none
#     }
# </style>
# """,
#     unsafe_allow_html=True,
# )
#     title = "Balanced Bytes"
#     st.markdown(f"<p style='margin-bottom:0px;margin-top:-70px;font-weight:bold;font-size:50px;color:#007DFF;text-align: center;'>{title}</p>", unsafe_allow_html=True)

  

#     col1,col2, buff1 = st.columns([1,1,1])

#     with col1:
#         name_val = st.text_input("Enter the Name", value='', placeholder='enter the name here')
#         weight_val = st.text_input("Enter the Weight(KG)", value=0)

#     with col2:
#         age_val = st.text_input("Enter the Age", value=0)
#         height_val = st.text_input("Enter the Height(CM)", value=0)


#     buff3,col4, buff2,col5=st.columns([0.2,1.6,1,2.2])

#     # with col5:
#     #     st_lottie('https://lottie.host/4659717d-9409-4dd1-9864-fdbdb233b7d8/p559s8xwiX.json', key="user")

#     with col4:
#         gender_val = st.radio("Pick your Gender",['Male','Female'])
#         st.divider()
#         activity_level_val = st.selectbox("What's your activity level?",['lightly active','moderately active','very active'])
#         food_allergies_val = st.multiselect("Do you have any dietary restrictions or food allergies?",['*Gluten Intolerance or Celiac Disease','Lactose Intolerance','Peanut Allergy','Tree Nut Allergy','Shellfish Allergy','Soy Allergy','Egg Allergy','Fish Allergy','Corn Allergy','Sesame Seed Allergy'])
#         eating_habits_val = st.selectbox("What are your typical eating habits?",['eat out frequently','cook at home','skip meals'])
#         goal_val = st.selectbox("What are your goals?",['Weight loss','weight maintenance','muscle gain','improved energy levels'])
#         diet_plan_val = st.selectbox("Are you currently following any specific diet plan?",['vegan','non-vegan','paleo'])
#         water_consump_val = st.selectbox("How much water do you drink?",['less','1 Litre','1.5 Litres','2 Litres','more'])
#         st.divider()
#         supplements_val = st.checkbox("Do you take any dietary supplements or vitamins regularly?")
#         pregnant_val = st.checkbox("Are you currently pregnant, breastfeeding, or planning to become pregnant?")
#         health_problems_val = st.multiselect(" Do you have any specific health conditions or concerns?",['Diabetes','hypertension','digestive issues'])
#         st.divider()  
#         if st.button("Submit details"):
#             if name_val != '':
#                 response = requests.post(
#                 'http://localhost:5000/post_data', 
#                 json={
#                     'name':name_val, 
#                     'age': age_val, 
#                     'height': height_val, 
#                     'weight': weight_val,
#                     'gender':gender_val,
#                     'activity_level':activity_level_val,
#                     'food_allergies':food_allergies_val,
#                     'eating_habits':eating_habits_val,
#                     'goal':goal_val,
#                     'water_consump':water_consump_val,
#                     'pregnant':pregnant_val,
#                     'diet_plan':diet_plan_val,
#                     'health_problems':health_problems_val,
#                     'supplements':supplements_val
#                     }
#                 )

#                 if response.status_code == 200:
#                     error1 = "successfull!!"
#                     st.markdown(f"<p style='color:#007DFF;font-size:20px;'>{error1}</p>", unsafe_allow_html=True)
#                     st.divider()
#                     st.write("To check a product?"
#                         f'''
#                             <a style="" target="_self" href="/options">
#                                 <button style="border:0px solid black;color:;border-radius:10px;padding: 0px 10px; background-color: white">
#                                     <p style="font-size:20px;color:#007DFF;"><u>click here</u></p>
#                             </button>
#                             </a>
#                         ''',unsafe_allow_html=True
#                         )

#                 else:
#                     error1 = "Couldn't upload data..."
#                     st.markdown(f"<p style='color:red;font-size:20px;'>{error1}</p>", unsafe_allow_html=True)
#             else:
#                 error2 = "Name cannot be empty..."
#                 st.markdown(f"<p style='color:orange;font-size:20px;'>{error2}</p>", unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()


import streamlit as st
import requests

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Balanced Bytes - Check Your Diet",
        page_icon='🌱',
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Define title
    st.title("Balanced Bytes")

    # Create columns for input fields
    col1, col2 = st.columns(2)
    
    # Input fields for personal details
    with col1:
        st.subheader("Personal Details")
        name_val = st.text_input("Name", "")
        weight_val = st.number_input("Weight (kg)", value=0)
    with col2:
        st.subheader("")
        age_val = st.number_input("Age", value=0)
        height_val = st.number_input("Height (cm)", value=0)

    # Activity level selection
    st.subheader("Activity Level")
    activity_level_val = st.radio("", ['Lightly Active', 'Moderately Active', 'Very Active'])

    # Dietary preferences and habits
    st.subheader("Dietary Preferences and Habits")
    gender_val = st.selectbox("Gender", ['Male', 'Female'])
    food_allergies_val = st.multiselect("Food Allergies", ['Gluten Intolerance', 'Lactose Intolerance', 'Peanut Allergy', 'Others'])
    eating_habits_val = st.selectbox("Eating Habits", ['Eats Out Frequently', 'Cooks at Home', 'Skips Meals'])
    goal_val = st.selectbox("Goals", ['Weight Loss', 'Weight Maintenance', 'Muscle Gain', 'Improved Energy Levels'])
    diet_plan_val = st.selectbox("Diet Plan", ['Vegan', 'Non-Vegan', 'Paleo'])
    water_consump_val = st.selectbox("Water Consumption", ['Less', '1 Litre', '1.5 Litres', '2 Litres', 'More'])
    supplements_val = st.checkbox("Take Dietary Supplements")

    # Pregnancy/Breastfeeding
    pregnant_val = st.checkbox("Pregnant/Breastfeeding")

    # Health problems
    st.subheader("Health Problems")
    health_problems_val = st.multiselect("Health Problems", ['Diabetes', 'Hypertension', 'Digestive Issues'])

    # Submit button
    if st.button("Submit", key="submit_button"):
        if name_val:
            response = requests.post(
                'http://127.0.0.1:5000/post_data', 
                json={
                    'name': name_val, 
                    'age': age_val, 
                    'height': height_val, 
                    'weight': weight_val,
                    'gender': gender_val,
                    'activity_level': activity_level_val,
                    'food_allergies': food_allergies_val,
                    'eating_habits': eating_habits_val,
                    'goal': goal_val,
                    'water_consump': water_consump_val,
                    'pregnant': pregnant_val,
                    'diet_plan': diet_plan_val,
                    'health_problems': health_problems_val,
                    'supplements': supplements_val
                }
            )
            if response.status_code == 200:
                st.success("Data uploaded successfully! 🎉")
            else:
                st.error("Failed to upload data...")
        else:
            st.warning("Name cannot be empty!")
        st.write("To check a product?"
                        f'''
                            <a style="" target="_self" href="/options">
                                <button style="border:0px solid black;color:;border-radius:10px;padding: 0px 10px; background-color: #0E1117">
                                    <p style="font-size:20px;color:#FF4B4B;"><u>click here</u></p>
                            </button>
                            </a>
                        ''',unsafe_allow_html=True
        )


if __name__ == "__main__":
    main()