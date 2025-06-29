import streamlit as st
from demo import area_of_circle

st.title("Hello World App")
st.write("This is a simple Streamlit app to demonstrate the setup.")

radius = st.slider("Select the radius of the circle:", min_value=0.0, max_value=100.0, value=1.0, step=0.1)

if st.button("Calculate Area"):
    area = area_of_circle(radius)
    st.write(f"The area of the circle is: {area:.2f}")