import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# =======================
# Load All Data
# =======================
df = pd.read_csv("historical_data.csv")
sarima = pd.read_csv("forecast_sarima.csv")
sarimax = pd.read_csv("forecast_sarimax.csv")
prophet = pd.read_csv("forecast_prophet.csv")
lstm = pd.read_csv("forecast_lstm.csv")
metrics = pd.read_csv("model_evaluation.csv")

# Convert date columns
df['Date'] = pd.to_datetime(df['Date'])
sarima['date'] = pd.to_datetime(sarima['date'])
sarimax['date'] = pd.to_datetime(sarimax['date'])
prophet['date'] = pd.to_datetime(prophet['date'])
lstm['date'] = pd.to_datetime(lstm['date'])

# =======================
# Page Title
# =======================
st.title("🚧 Forecasting Tol Road Revenue (2019–2024)")
st.markdown("""
Forecasting revenue jalan tol berdasarkan data mingguan (2019–2023) menggunakan:
- **SARIMA**
- **SARIMAX (dengan traffic volume)**
- **Prophet**
- **LSTM**

Prediksi dilakukan selama **1 tahun ke depan (2024)**.
""")

# =======================
# KPI Section
# =======================
total_weeks = len(df)
total_revenue = df['Revenue'].sum()
avg_weekly = df['Revenue'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Weeks", total_weeks)
col2.metric("Total Revenue", f"{total_revenue:,.0f}")
col3.metric("Rata-rata per Minggu", f"{avg_weekly:,.0f}")

# =======================
# Historical Revenue Visualization
# =======================
st.subheader("📈 Revenue Historis (2019–2023)")
selected_year = st.selectbox("Pilih Tahun", sorted(df['Date'].dt.year.unique()))
filtered = df[df['Date'].dt.year == selected_year]
fig = px.line(filtered, x='Date', y='Revenue', title=f'Revenue Mingguan Tahun {selected_year}')
st.plotly_chart(fig, use_container_width=True)

# =======================
# Optional: Show Traffic Volume
# =======================
st.subheader("🚗 Traffic Volume Historis")
if 'Traffic_Volume' in df.columns:
    if st.checkbox("Tampilkan Grafik Traffic Volume"):
        fig_vol = px.line(df, x='Date', y='Traffic_Volume', title="Volume Lalu Lintas Mingguan")
        st.plotly_chart(fig_vol, use_container_width=True)

# =======================
# Forecasting Chart
# =======================
st.subheader("🔮 Forecasting 2024 (1 Tahun ke Depan)")
model_option = st.selectbox("Pilih Model Forecasting", [
    "SARIMA", "SARIMAX (w/ traffic volume)", "Prophet", "LSTM"
])

if model_option == "SARIMA":
    model_data = sarima
elif model_option.startswith("SARIMAX"):
    model_data = sarimax
elif model_option == "Prophet":
    model_data = prophet
else:
    model_data = lstm

# Filter forecast hanya 2024
forecast = model_data[model_data['date'].dt.year == 2024]
historical = df[df['Date'] < '2024']

fig2 = px.line(historical, x='Date', y='Revenue', labels={'Revenue': 'Revenue'}, title="Historis + Forecast (2024)")
fig2.add_scatter(x=forecast['date'], y=forecast['forecast'], mode='lines', name='Forecast')
st.plotly_chart(fig2, use_container_width=True)

# =======================
# Model Comparison Table
# =======================
st.subheader("📊 Perbandingan Akurasi Model")
metrics['Model'] = metrics['Model'].replace({
    'SARIMAX': 'SARIMAX (w/ traffic volume)'
})
st.dataframe(metrics.style.format({
    "RMSE": "{:,.0f}",
    "MAE": "{:,.0f}",
    "MAPE": "{:.2f}%"
}))

# =======================
# Download Forecast
# =======================
st.subheader("⬇️ Download Forecast Result")
csv = model_data.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download Forecast CSV",
    data=csv,
    file_name=f"forecast_{model_option.lower().split()[0]}.csv",
    mime="text/csv"
)
