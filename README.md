# 🏎️ Formula 1 Data Analysis Dashboard

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://f1analysis-apw4r9dgzqfwx8vxbpardu.streamlit.app)
![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-2.0+-brightgreen.svg)

An interactive dashboard for analyzing Formula 1 historical data with driver/constructor performance metrics and race visualizations.

## ✨ Features
- Driver/constructor performance analytics
- Circuit speed comparisons
- Interactive race telemetry
- Pit stop efficiency analysis

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly, Matplotlib, Seaborn

## 📂 Data Structure
```text
data/
├── drivers.csv
├── constructors.csv
├── races.csv
├── results.csv
├── qualifying.csv
└── lap_times.csv
```

## 🚀 Quick Start
```bash
# Clone repo
git clone https://github.com/yourusername/f1-dashboard.git
cd f1-dashboard

# Install dependencies
pip install -r requirements.txt

# Launch app
streamlit run app.py
```

## 📊 Example Query
```python
# Get top 10 winning drivers
winners = results[results['position'] == 1]
top_drivers = winners['driverId'].value_counts().head(10)
```

## 📜 License
MIT License - See [LICENSE](LICENSE) for details.
