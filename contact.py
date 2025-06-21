import streamlit as st

# Data for specialists
specialists = {
    "Brain Tumor Specialists": [
        {"name": "Dr. V. P. Singh", "institution": "Medanta - The Medicity, Gurgaon", "phone": "+91 124 4141414", "website": "medanta.org"},
        {"name": "Dr. B. K. Misra", "institution": "Hinduja Hospital, Mumbai", "phone": "+91 22 24452222", "website": "hindujahospital.com"}
    ],
    "Pneumonia Specialists": [
        {"name": "Dr. Randeep Guleria", "institution": "All India Institute of Medical Sciences (AIIMS), New Delhi", "phone": "+91 11 26588500", "website": "aiims.edu"},
        {"name": "Dr. Arvind Kumar", "institution": "Sir Ganga Ram Hospital, New Delhi", "phone": "+91 11 25750000", "website": "sgrh.com"}
    ],
    "Skin Cancer Specialists": [
        {"name": "Dr. Rashmi Taneja", "institution": "Fortis Hospital, Vasant Kunj, New Delhi", "phone": "+91 11 42776222", "website": "fortishealthcare.com"},
        {"name": "Dr. Sandeep Gupta", "institution": "Apollo Hospital, Bangalore", "phone": "+91 80 26304050", "website": "apollohospitals.com"}
    ]
}

# Sidebar
st.sidebar.title("Specialists Finder")
selected_specialization = st.sidebar.selectbox("Select Specialization", list(specialists.keys()))

# Display specialists
st.title(selected_specialization)
for specialist in specialists[selected_specialization]:
    st.write("- **Name:**", specialist["name"])
    st.write("  **Institution:**", specialist["institution"])
    st.write("  **Phone:**", specialist["phone"])
    st.write("  **Website:**", specialist["website"])
