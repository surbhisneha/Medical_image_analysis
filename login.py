import streamlit as st

def authenticate(username, password):
    # Dummy authentication function
    if username == "admin" and password == "password":
        return True
    else:
        return False
    

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.shutterstock.com/image-photo/doctor-medical-blue-background-260nw-76677112.jpg");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.success("Login successful!")
            # Redirect to the dashboard or another page
        else:
            st.error("Invalid username or password. Please try again.")

if __name__ == "__main__":
    main()
