import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Regional Sales & Orders Analysis")

# -------------------------
# Create DataFrame
# -------------------------
df = pd.DataFrame({
    'Region': ['North', 'South', 'North', 'South', 'East'],
    'Sales': [100, 150, 200, 180, 120],
    'Orders': [5, 8, 10, 7, 6]
})

st.subheader("Original Data")
st.dataframe(df)

# -------------------------
# Grouped Calculations
# -------------------------
total = df.groupby('Region')['Sales'].sum().reset_index()
total.index = range(1, len(total) + 1)

avg = df.groupby('Region')['Sales'].mean().reset_index()
avg.index = range(1, len(avg) + 1)

summary = df.groupby('Region').agg({
    'Sales': ['sum', 'mean', 'count'],
    'Orders': 'sum'
}).reset_index()

summary.index = range(1, len(summary) + 1)

# -------------------------
# Display Grouped Tables
# -------------------------
st.subheader("Total Sales by Region")
st.dataframe(total)

st.subheader("Average Sales by Region")
st.dataframe(avg)

st.subheader("Summary Table")
st.dataframe(summary)

# -------------------------
# Sales by Region
# -------------------------
st.subheader("Sales by Region")
fig1, ax1 = plt.subplots()
sns.barplot(data=df, x='Region', y='Sales', ax=ax1)
ax1.set_title("Sales by Region")
st.pyplot(fig1)

# -------------------------
# Orders by Region
# -------------------------
st.subheader("Orders by Region")
fig2, ax2 = plt.subplots()
sns.barplot(data=df, x='Region', y='Orders', ax=ax2)
ax2.set_title("Orders by Region")
st.pyplot(fig2)

# -------------------------
# Sales Distribution
# -------------------------
st.subheader("Sales Distribution")
fig3, ax3 = plt.subplots()
sns.histplot(data=df, x='Sales', bins=5, kde=True, ax=ax3)
ax3.set_title("Distribution of Sales")
st.pyplot(fig3)

# -------------------------
# Sales vs Orders
# -------------------------
st.subheader("Sales vs Orders")
fig4, ax4 = plt.subplots()
sns.scatterplot(data=df, x='Orders', y='Sales', hue='Region', ax=ax4)
ax4.set_title("Sales vs Orders by Region")
st.pyplot(fig4)
