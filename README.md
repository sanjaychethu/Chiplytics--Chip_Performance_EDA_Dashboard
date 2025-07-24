# 🔬 Chiplytics – Semiconductor Performance EDA Dashboard

**Chiplytics** is a semiconductor analytics project built to analyze chip telemetry data using scalable data engineering techniques. It contains a **PySpark-based data processing notebook** as the core EDA pipeline and an interactive **Streamlit dashboard** to visualize chip performance insights.

This project simulates real-world chip logs to monitor power, temperature, and timing errors — ideal for debugging, performance tuning, and yield improvement in semiconductor design.

---

## 🎯 What This Project Includes

1. 📓 `PySpark_Full_Chip_Log_EDA_Pipeline.ipynb` – **Core project logic**
   - Scalable analysis of chip logs using PySpark
   - Feature aggregation and anomaly detection
   - Designed for use in large-scale environments (e.g., Azure, Databricks)

2. 💻 `app.py` – **Interactive Streamlit dashboard**
   - Allows filtering by chip ID and temperature
   - Displays real-time trends, summary stats, and correlation insights
   - Built as a user-facing dashboard for demo/presentation

---

## 🛠️ Tech Stack

| Tool         | Purpose                            |
|--------------|------------------------------------|
| **PySpark**  | Scalable log processing (main logic) |
| **Pandas**   | Lightweight EDA (dashboard)         |
| **Streamlit**| Dashboard UI                        |
| **Matplotlib / Seaborn** | Visualizations         |
| *(Future-ready)* **Azure / Databricks** | Cloud scaling support |

---

## 📊 Key Features

- Chip-wise performance summaries (avg. power/temp/errors)
- Lineplots of temperature trends over time
- Boxplots of power consumption
- Correlation heatmaps for telemetry metrics
- Interactive filters for chip ID and temperature threshold

---

## 📁 Dataset

The dataset is synthetically generated and contains over **10,000 entries**:

| Column | Description |
|--------|-------------|
| `timestamp` | Time of reading (1-minute intervals) |
| `chip_id`   | Unique ID per chip (CHIP_1 to CHIP_100) |
| `power_mw`  | Power usage in milliwatts |
| `temperature_c` | Temperature in Celsius |
| `timing_errors` | Count of timing errors |

> 🗂️ File: `chip_performance_logs.csv`

---

## 🧠 Full Project Notebook

📓 [`PySpark_Full_Chip_Log_EDA_Pipeline.ipynb`](./PySpark_Full_Chip_Log_EDA_Pipeline.ipynb)

**What it does:**
- Loads large-scale logs with PySpark
- Aggregates chip-level performance stats
- Identifies outliers in temperature/power/errors
- Designed for real-time and cloud-based deployments
- Suitable for Databricks, HDFS, or Azure Data Lake


---

## 🌐 Streamlit Dashboard

🔗 [Live Demo](https://chiplytics.streamlit.app/)

📄 File: [`app.py`](./app.py)

- Frontend dashboard to present insights
- Filters for chip ID and temperature
- Real-time visualizations (boxplots, linecharts, heatmap)

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/sanjaychethu/pipeline.git
cd pipeline

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
