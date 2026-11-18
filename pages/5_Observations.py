
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Observations", page_icon="📈", layout="wide")

st.title("📈 Observations and Analysis")
st.caption("Analysis of Gradient Descent simulation results")
st.divider()

st.subheader("1. Observation Parameters")

learning_rate = st.selectbox(
    "Select Learning Rate",
    [0.001, 0.005, 0.01, 0.05]
)

iterations = st.selectbox(
    "Select Number of Iterations",
    [50, 100, 200, 500]
)

np.random.seed(42)
X = np.linspace(1, 10, 30)
y = 3 * X + 5 + np.random.normal(0, 2, 30)

m = 0.0
b = 0.0
n = len(X)

records = []

for i in range(iterations):
    prediction = m * X + b
    error = prediction - y

    loss = np.mean(error ** 2)

    dm = (2 / n) * np.sum(error * X)
    db = (2 / n) * np.sum(error)

    m -= learning_rate * dm
    b -= learning_rate * db

    records.append({
        "Iteration": i + 1,
        "Slope": m,
        "Intercept": b,
        "MSE Loss": loss
    })

df = pd.DataFrame(records)

st.subheader("2. Iteration-wise Observations")

st.dataframe(
    df.style.format({
        "Slope": "{:.4f}",
        "Intercept": "{:.4f}",
        "MSE Loss": "{:.4f}"
    }),
    use_container_width=True
)

st.subheader("3. Observation Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Initial Loss", f"{df['MSE Loss'].iloc[0]:.4f}")
col2.metric("Final Loss", f"{df['MSE Loss'].iloc[-1]:.4f}")
col3.metric("Total Iterations", iterations)

st.subheader("4. Analysis")

if df["MSE Loss"].iloc[-1] < df["MSE Loss"].iloc[0]:
    st.success(
        "The loss function decreased during optimization. "
        "The model parameters moved towards a better solution."
    )
else:
    st.warning(
        "The loss did not decrease. Try a different learning rate."
    )

st.divider()
st.caption("Observation data is generated using the selected parameters.")
