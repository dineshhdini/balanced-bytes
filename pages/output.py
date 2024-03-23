import streamlit as st 
import requests

st.markdown("""<style>
    [data-testid="collapsedControl"] {
        display: none}</style>""",
    unsafe_allow_html=True,
)
st.title("Information on the product")

response = requests.get('http://localhost:5000/output')
data = response.json()
name_val = data['ingredients']


st.write(f"""
<body>
    <table style="width:100%;">
        <tr>
            <td>
                <h3 style="color:;">Ingredients </h3>
            </td>
        </tr>
        <tr>
            <td>
                <p>{name_val}</p>
            </td>
        </tr>
    </table>
         <br>
    <table style="width:100%;">
        <tr>
            <td>
                <h3 style="color:;">Time to eat </h3>
            </td>
        </tr>
        <tr>
            <td>
                <p>
Lay's potato chips varieties contain limited nutrition, with vitamin C being the highest at 10% of the daily requirement per serving. Salt content is notably high, with up to 380 mg of sodium per serving. Ingredients vary across varieties, but Lay's Classic Potato chips transitioned from hydrogenated oil to sunflower, corn, and/or canola oil in 2003.</p>
            </td>
        </tr>
    </table>
         <br>
    <table style="width:100%;">
        <tr>
            <td>
                <h3 style="color:;">Quantity for Consumption </h3>
            </td>
        </tr>
        <tr>
            <td>
                <p>
Lay's potato chips varieties contain limited nutrition, with vitamin C being the highest at 10% of the daily requirement per serving. Salt content is notably high, with up to 380 mg of sodium per serving. Ingredients vary across varieties, but Lay's Classic Potato chips transitioned from hydrogenated oil to sunflower, corn, and/or canola oil in 2003.</p>
            </td>
        </tr>
    </table>
</body>
""", unsafe_allow_html=True)