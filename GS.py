import streamlit as st
import pandas as pd
import time

# URL of the Google Sheet
sheet_url = "https://docs.google.com/spreadsheets/d/1IPVWYgvF-WKStU4Lk545mXzhIb9LB8HggZ9zUY-3quc/gviz/tq?tqx=out:csv&gid=0"

# Set page configuration
st.set_page_config(
    page_title="Real-Time Dashboard",  # Title of the tab
    page_icon="📊",                    # Emoji or custom icon as the tab icon
    layout="wide"                      # Wide layout for better visualization
)

# Set background image using custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://news.umpsa.edu.my/sites/default/files/gallery-article/UMPSA%20Solar_0.jpg');
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        height: 100%;
        width: 100%;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Load data
@st.cache_data(ttl=1)  # Cache the data with a 1-second TTL
def load_data(url):
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return None

# Main app
st.title("Advanced Multi-Sensor Data Acquisition and Logging  System")

# Container for the data table
data_container = st.empty()  # Placeholder for dynamic updates

# Real-time update loop
try:
    while True:
        # Load data
        data = load_data(sheet_url)

        if data is not None:
            # Display the dataset dynamically with customized width
            data_container.dataframe(
                data, 
                use_container_width=True  # Makes the table expand to the container's width
            )
        else:
            data_container.error("No data available to display.")

        # Wait for 1 second before updating
        time.sleep(1)
except KeyboardInterrupt:
    st.write("Stopped real-time updates.")
