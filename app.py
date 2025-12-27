import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Farm Market Link", layout="centered")

st.title("🌾 Farm Market Link")
st.subheader("Agricultural Pricing and Demand Forecast")

# Load dataset
data = pd.read_csv("clean_market_data.csv")

# Dropdowns
group = st.selectbox(
    "Select Commodity Group",
    data["Commodity Group"].unique()
)

commodity = st.selectbox(
    "Select Commodity",
    data[data["Commodity Group"] == group]["Commodity"].unique()
)

# Filter data
filtered = data[
    (data["Commodity Group"] == group) &
    (data["Commodity"] == commodity)
]

st.write("### Market Data")
st.dataframe(filtered)

# Chart
st.write("### Price & Demand Overview")
fig, ax = plt.subplots()
ax.bar(
    ["Average Price", "Average Arrival"],
    [
        filtered["Average Price"].values[0],
        filtered["Average Arrival"].values[0]
    ]
)
st.pyplot(fig)
