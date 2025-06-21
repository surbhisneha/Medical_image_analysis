import streamlit as st
import pages.login as login
import pages.contact as contact
import pages.cure as cure
import pages.hospital as hospital
import pages.image as image
import pages.pneumonia as pneumonia
import pages.skin_cancer as skin_cancer

# Welcome message and introduction
st.title("Welcome to the Medical Image Analysis")
st.write("This app provides tools for medical image analysis, login functionality, contact information, and access to resources related to brain tumors, pneumonia, medical cures, and hospitals.")

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Login", "Contact", "Cures", "Hospital", "Brain Tumor", "Pneumonia", "About Brain Tumor", "About Pneumonia"])

# Load the selected page
if page == "Home":
    st.write("Please select a page from the sidebar.")
elif page == "About":
    st.title("About")
    st.write("This is the About page. Here you can provide information about your application.")
elif page == "Login":
    login.run()
elif page == "Contact":
    contact.run()
elif page == "Cures":
    cure.run()
elif page == "Hospital":
    hospital.run()
elif page == "Brain Tumor":
    image.run()
elif page == "Pneumonia":
    pneumonia.run()
elif page == "About Brain Tumor":
    st.title("About Brain Tumor")
    st.write("Information about brain tumors goes here.")
elif page == "About Pneumonia":
    st.title("About Pneumonia")
    st.write("Information about pneumonia goes here.")
elif page == "About Skin Cancer":
    st.title("About Skin Cancer")
    st.write("Information about Skin Cancer goes here.")   
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url("https://img.freepik.com/free-photo/medical-stethoscope-isolated-with-black-background-medical-concept-stethoscope-black-background-with-space-text-health-concept-medical-conceptual_1391-769.jpg?w=996&t=st=1717869829~exp=1717870429~hmac=1459f3d3b6a12f31cc86f174fb6292fec37ff9697a431a08cd060d712d71fde6");
#         background-size: cover;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )