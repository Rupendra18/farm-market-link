import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(
    page_title="Farm Market Link",
    page_icon="🌾",
    layout="wide"
)

# Title
st.title("🌾 Farm Market Link")
st.markdown("### Agricultural Pricing and Demand Forecast Dashboard")

# Load data
data = pd.read_csv("clean_market_data.csv")

# Sidebar
st.sidebar.header("🔍 Select Options")

group = st.sidebar.selectbox(
    "Commodity Group",
    data["Commodity Group"].unique()
)

commodity = st.sidebar.selectbox(
    "Commodity",
    data[data["Commodity Group"] == group]["Commodity"].unique()
)

# Filter data
filtered = data[
    (data["Commodity Group"] == group) &
    (data["Commodity"] == commodity)
]

price = filtered["Average Price"].values[0]
arrival = filtered["Average Arrival"].values[0]

# Main layout
col1, col2 = st.columns(2)

with col1:
    st.metric(label="💰 Average Price", value=f"₹ {price}")

with col2:
    st.metric(label="📦 Average Arrival (Demand)", value=f"{arrival}")

st.markdown("---")

# Chart section
st.subheader("📊 Price vs Demand Overview")

fig, ax = plt.subplots(figsize=(6,4))
ax.bar(
    ["Average Price", "Average Arrival"],
    [price, arrival],
    color=["#4CAF50", "#2196F3"]
)
ax.set_ylabel("Value")
ax.set_title("Market Analysis")
st.pyplot(fig)

# Data table
st.subheader("📋 Market Data")
st.dataframe(filtered)

# Footer
st.markdown("---")
st.caption(
    "Farm Market Link | Developed as an academic project using Streamlit Cloud"
)

