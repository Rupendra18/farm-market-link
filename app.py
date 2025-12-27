import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os

# Page configuration
st.set_page_config(
    page_title="Farm Market Link",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 Farm Market Link")
st.markdown("### Agricultural Pricing and Demand Forecast Dashboard")

# Load dataset
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

# 📸 IMAGE SECTION
image_path = f"images/{commodity.lower()}.jpg"

if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, caption=commodity, width=300)
else:
    st.info("Image not available for this commodity")

# Metrics
col1, col2 = st.columns(2)
with col1:
    st.metric("💰 Current Average Price", f"₹ {price}")
with col2:
    st.metric("📦 Average Arrival (Demand)", arrival)

st.markdown("---")

# 📈 Line chart
st.subheader("📈 Price & Demand Trend")

future_points = ["Current", "Next Month"]
price_trend = [price, price * 1.05]
demand_trend = [arrival, arrival * 1.03]

fig, ax = plt.subplots()
ax.plot(future_points, price_trend, marker="o", label="Price")
ax.plot(future_points, demand_trend, marker="o", label="Demand")
ax.legend()
ax.set_title("Expected Trend")
st.pyplot(fig)

# 🔮 Prediction button
st.subheader("🔮 Future Price Prediction")

if st.button("Predict Next Month Price"):
    predicted_price = round(price * 1.05, 2)
    st.success(f"📊 Predicted Price for Next Month: ₹ {predicted_price}")

# Table
st.subheader("📋 Market Data")
st.dataframe(filtered)

st.markdown("---")
st.caption("Farm Market Link | Academic Project | Image-based UI enhancement")
