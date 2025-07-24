import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# App Title and Description
st.set_page_config(page_title="Chip Performance Dashboard", layout="wide")
st.title("📈 Chip Performance EDA Dashboard")
st.markdown("Analyze power, temperature, and timing error metrics for simulated semiconductor chip logs.")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("chip_performance_logs.csv", parse_dates=["timestamp"])
    return df

df = load_data()

# Sidebar filters
chip_list = df["chip_id"].unique()
selected_chip = st.sidebar.selectbox("Select Chip ID", sorted(chip_list))
selected_range = st.sidebar.slider("Select Temperature Threshold", 60, 100, (70, 90))

# Filter data
filtered_df = df[(df["chip_id"] == selected_chip) & 
                 (df["temperature_c"] >= selected_range[0]) &
                 (df["temperature_c"] <= selected_range[1])]

# Summary statistics
st.subheader(f"📊 Summary Statistics for {selected_chip}")
col1, col2, col3 = st.columns(3)
col1.metric("Average Power (mW)", f"{filtered_df['power_mw'].mean():.2f}")
col2.metric("Avg Temp (°C)", f"{filtered_df['temperature_c'].mean():.2f}")
col3.metric("Avg Timing Errors", f"{filtered_df['timing_errors'].mean():.2f}")

# Line plot: Temperature over time
st.subheader("🌡️ Temperature Over Time")
fig1, ax1 = plt.subplots()
sns.lineplot(data=filtered_df, x="timestamp", y="temperature_c", ax=ax1)
ax1.set_title("Temperature Over Time")
st.pyplot(fig1)

# Boxplot: Power distribution
st.subheader("⚡ Power Distribution")
fig2, ax2 = plt.subplots()
sns.boxplot(data=filtered_df, y="power_mw", ax=ax2)
ax2.set_title("Power (mW) Distribution")
st.pyplot(fig2)

# Heatmap of correlations
st.subheader("📌 Correlation Heatmap")
fig3, ax3 = plt.subplots()
corr = filtered_df[["power_mw", "temperature_c", "timing_errors"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax3)
st.pyplot(fig3)

# Footer
st.markdown("---")
st.markdown("✅ Built with Streamlit | Project by V Sanjay")
