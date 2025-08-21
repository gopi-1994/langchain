import streamlit as st
import helper
        

st.title("Restaurant Menu Generator")
st.sidebar.header("Menu")
cusine = st.sidebar.selectbox("Select a Cusine",("Indian", "Chinese", "Italian", "Mexican"))
if cusine:
    result = helper.generate_restaurant_name_and_items(cusine)
    st.header(result['restaurant_name'])
    menu_items = result['menu_items'].split(',')
    st.write("**Menu items:**")
    for item in menu_items:
        st.write(f"- {item.strip()}")