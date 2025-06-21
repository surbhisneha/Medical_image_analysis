import streamlit as st
import requests

# Function to get hospitals near a location using Google Places API
def get_hospitals(lat, lon, radius, api_key):
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lon}&radius={radius}&type=hospital&key={api_key}'
    response = requests.get(url).json()
    return response.get('results', [])

# Function to display hospital information
def display_hospitals(hospitals):
    if not hospitals:
        st.write("No hospitals found nearby.")
    else:
        st.write(f"Top Hospitals Nearby:")
        for hospital in hospitals:
            st.write(f"- {hospital['name']}")
            if 'vicinity' in hospital:
                st.write(f"  Address: {hospital['vicinity']}")
            st.write("---")

def main():
    st.title("Find Nearby Hospitals")

    st.write("Enter your destination location (latitude and longitude):")
    lat = st.number_input("Latitude")
    lon = st.number_input("Longitude")

    radius_km = st.slider("Select range for searching hospitals (in kilometers):", min_value=1, max_value=10, step=1)

    if st.button("Find Hospitals"):
        st.write(f"Searching for hospitals near Latitude {lat}, Longitude {lon} within {radius_km} km...")

        # Google Places API for finding hospitals
        google_places_api_key = 'YOUR_GOOGLE_PLACES_API_KEY'  # Replace with your actual Google Places API key
        radius_meters = radius_km * 1000  # Convert km to meters
        hospitals = get_hospitals(lat, lon, radius_meters, google_places_api_key)
        display_hospitals(hospitals)

if __name__ == "__main__":
    main()
