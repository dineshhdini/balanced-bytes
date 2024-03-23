import streamlit as st
from flask import Flask, json
import requests

def login_page():
    st.set_page_config(page_title="login", page_icon="🌱")
    st.title("Login page")
    st.markdown("""<style>
        [data-testid="collapsedControl"] {
            display: none}</style>""",
        unsafe_allow_html=True,
    )
    st.divider()

    st.subheader("Provide the below details...")
    email_val = st.text_input("Enter your email here")
    password_val = st.text_input("Enter your password")

    if st.button("sign-in"):
        response = requests.post('http://localhost:5000/login', json={
            'email':email_val,
            'password':password_val
        })
        if response.status_code == 200:
            success = "Successfull!!!"
            st.markdown(f"<p style='color:#00ff44;font-size:20px;'>{success}</p>", unsafe_allow_html=True)
            st.write("To enter your details regarding your health and diet..?"
                f'''
                    <a style="" target="_self" href="/details">
                        <button style="border:0px solid black;color:#00ff44;border-radius:10px;padding: 0px 10px; background-color: #0b001b">
                            <p style="font-size:17px;color:$00ff44;"><u>click here</u></p>
                        </button>
                    </a>
                ''',unsafe_allow_html=True
            )
        else:
            st.write("error")
    st.write("Don't have an Account?"
        f'''
            <a style="" target="_self" href="/signin_page">
                <button style="border:0px solid black;color:#00ff44;border-radius:10px;padding: 0px 10px; background-color: #0b001b">
                    <p style="font-size:17px;color:$00ff44;"><u>click here</u></p>
                </button>
            </a>
        ''',unsafe_allow_html=True
    )
    st.divider()

login_page()