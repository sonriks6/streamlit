# 🔥 1.88 Million US Wildfires Dashboard & Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://wildfire.streamlit.app/)

Welcome to the **US Wildfires Research Project**, an interactive dashboard built with [Streamlit](https://streamlit.io). This application provides rich geographical visualizations and machine learning-powered predictions based on the Kaggle [1.88 Million US Wildfires](https://www.kaggle.com/datasets/rtatman/188-million-us-wildfires) dataset (covering data from 1992 to 2015).

---

## 📖 Overview

The goal of this project is to explore and predict wildfire causes across the United States. We have enhanced the original dataset by incorporating County, Population, Area information, and the mean temperature at the county level.

### Key Features

- **📈 Machine Learning Model**: A trained Random Forest Classifier capable of predicting the cause of a fire (Natural, Accidental, or Malicious) based on geographical data and timing.
- **🌍 Map Visualization**: Interactive map visualizations allowing users to explore fire occurrences by year and fire size classification (NWCG standards).
- **📊 Choropleth Map**: Deep dive into county-level granularity to visualize fire frequency and density across different regions over time using Plotly.
- **🔥 Conclusions**: A summary of our findings regarding fire progression, seasonality, and human impacts, alongside reflections on the data analysis journey.

## 🛠️ Technology Stack

- **Frontend/UI:** [Streamlit](https://streamlit.io/) (Multipage App)
- **Data Processing:** Pandas, NumPy, PyArrow
- **Machine Learning:** Scikit-Learn
- **Visualizations:** Plotly, Streamlit Native Maps

## 🚀 Getting Started Locally

To run this application on your local machine, follow these steps:

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository-url>
   cd streamlit
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit application**:
   ```bash
   streamlit run Hello.py
   ```

## 👥 The Team

This project was developed as part of the Data Analyst program by DataScientest.
- **Cecile Sinna** 💡
- **Jean Christophe Theault** 💻
- **Santiago Rodriguez Diaz** 🧠

Thank you for visiting!
