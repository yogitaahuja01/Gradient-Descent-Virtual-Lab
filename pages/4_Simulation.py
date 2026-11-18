
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Gradient Descent Simulation",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Interactive Gradient Descent Simulation")
st.caption("Explore Linear Regression optimization step by step")
st.divider()

# --------------------------------------------------
# 1. DATASET
# --------------------------------------------------

st.sidebar.header("Simulation Settings")

dataset_option = st.sidebar.radio(
    "Choose Dataset",
    ["Sample Dataset", "Upload CSV Dataset"]
)

uploaded_file = None

if dataset_option == "Upload CSV Dataset":
    uploaded_file = st.sidebar.file_uploader(
        "Upload CSV file",
        type=["csv"]
    )

if uploaded_file is not None:
    try:
        uploaded_data = pd.read_csv(uploaded_file)
        numeric_columns = uploaded_data.select_dtypes(
            include=np.number
        ).columns.tolist()

        if len(numeric_columns) < 2:
            st.error("CSV must contain at least two numeric columns.")
            st.stop()

        x_column = st.sidebar.selectbox(
            "Select X (Input)",
            numeric_columns,
            index=0
        )

        y_column = st.sidebar.selectbox(
            "Select Y (Output)",
            numeric_columns,
            index=1
        )

        clean_data = uploaded_data[[x_column, y_column]].dropna()

        if len(clean_data) < 2:
            st.error("At least two valid data rows are required.")
            st.stop()

        X = clean_data[x_column].to_numpy(dtype=float)
        y = clean_data[y_column].to_numpy(dtype=float)

        if not np.all(np.isfinite(X)) or not np.all(np.isfinite(y)):
            st.error("Dataset contains invalid numeric values.")
            st.stop()

        if np.ptp(X) == 0:
            st.error("The input column must contain different values.")
            st.stop()

        dataset_name = uploaded_file.name

    except Exception as error:
        st.error(f"Unable to read CSV: {error}")
        st.stop()

else:
    np.random.seed(42)
    X = np.linspace(1, 10, 30)
    y = 3 * X + 5 + np.random.normal(0, 2, 30)
    dataset_name = "Generated Sample Dataset"

data_id = (
    f"{dataset_name}-{len(X)}-"
    f"{np.sum(X):.6f}-{np.sum(y):.6f}"
)

st.subheader("1. Dataset")

st.caption(f"Selected dataset: {dataset_name}")

data = pd.DataFrame({
    "Input (X)": X,
    "Output (Y)": y
})

st.dataframe(data, use_container_width=True)

# --------------------------------------------------
# 2. PARAMETERS
# --------------------------------------------------

st.sidebar.divider()
st.sidebar.subheader("Optimization Parameters")

learning_rate = st.sidebar.number_input(
    "Learning Rate",
    min_value=0.0001,
    max_value=0.1,
    value=0.005,
    step=0.001,
    format="%.4f"
)

max_iterations = st.sidebar.slider(
    "Maximum Iterations",
    min_value=10,
    max_value=1000,
    value=100,
    step=10
)

initial_m = st.sidebar.number_input(
    "Initial Slope (m)",
    value=0.0
)

initial_b = st.sidebar.number_input(
    "Initial Intercept (b)",
    value=0.0
)

# --------------------------------------------------
# 3. GRADIENT DESCENT FUNCTIONS
# --------------------------------------------------

def calculate_loss(m, b, X, y):
    predictions = m * X + b
    return np.mean((predictions - y) ** 2)


def initialize_simulation():
    return {
        "m": float(initial_m),
        "b": float(initial_b),
        "iteration": 0,
        "history": [{
            "Iteration": 0,
            "Slope": float(initial_m),
            "Intercept": float(initial_b),
            "MSE Loss": float(
                calculate_loss(initial_m, initial_b, X, y)
            )
        }],
        "status": "Ready"
    }


if (
    "sim_data_id" not in st.session_state
    or st.session_state.sim_data_id != data_id
):
    st.session_state.sim_data_id = data_id
    st.session_state.simulation = initialize_simulation()

if "simulation" not in st.session_state:
    st.session_state.simulation = initialize_simulation()

sim = st.session_state.simulation

def perform_one_step():
    m = sim["m"]
    b = sim["b"]
    n = len(X)

    predictions = m * X + b
    error = predictions - y

    dm = (2 / n) * np.sum(error * X)
    db = (2 / n) * np.sum(error)

    new_m = m - learning_rate * dm
    new_b = b - learning_rate * db

    if not np.isfinite(new_m) or not np.isfinite(new_b):
        sim["status"] = "Diverged"
        return

    new_loss = calculate_loss(new_m, new_b, X, y)

    if not np.isfinite(new_loss) or new_loss > 1e15:
        sim["status"] = "Diverged"
        return

    sim["m"] = new_m
    sim["b"] = new_b
    sim["iteration"] += 1

    sim["history"].append({
        "Iteration": sim["iteration"],
        "Slope": new_m,
        "Intercept": new_b,
        "MSE Loss": new_loss
    })

    sim["status"] = (
        "Completed"
        if sim["iteration"] >= max_iterations
        else "Running"
    )


# --------------------------------------------------
# 4. SIMULATION CONTROLS
# --------------------------------------------------

st.divider()
st.subheader("2. Run Your Experiment")

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("▶ Run All", use_container_width=True):
        while (
            sim["iteration"] < max_iterations
            and sim["status"] != "Diverged"
        ):
            perform_one_step()

        st.rerun()

with c2:
    if st.button("⏭ Run One Step", use_container_width=True):
        if sim["iteration"] < max_iterations:
            if sim["status"] != "Diverged":
                perform_one_step()
        st.rerun()

with c3:
    if st.button("↻ Reset", use_container_width=True):
        st.session_state.simulation = initialize_simulation()
        st.rerun()

# --------------------------------------------------
# 5. LIVE RESULTS
# --------------------------------------------------

st.divider()
st.subheader("3. Live Simulation Results")

m = sim["m"]
b = sim["b"]
loss = calculate_loss(m, b, X, y)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Current Iteration", sim["iteration"])
c2.metric("Current Slope", f"{m:.5f}")
c3.metric("Current Intercept", f"{b:.5f}")
c4.metric("Current MSE Loss", f"{loss:.5f}")

if sim["status"] == "Completed":
    st.success("Maximum iterations completed.")

elif sim["status"] == "Diverged":
    st.error(
        "The algorithm diverged. Reduce the learning rate "
        "and reset the simulation."
    )

else:
    st.info(f"Simulation status: {sim['status']}")

# --------------------------------------------------
# 6. REGRESSION GRAPH
# --------------------------------------------------

st.divider()
st.subheader("4. Regression Line Visualization")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=X,
    y=y,
    mode="markers",
    name="Actual Data"
))

fig.add_trace(go.Scatter(
    x=X,
    y=m * X + b,
    mode="lines",
    name="Predicted Regression Line"
))

fig.update_layout(
    xaxis_title="Input X",
    yaxis_title="Output Y",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# 7. LOSS GRAPH
# --------------------------------------------------

st.subheader("5. Loss Convergence")

history_df = pd.DataFrame(sim["history"])

loss_fig = go.Figure()

loss_fig.add_trace(go.Scatter(
    x=history_df["Iteration"],
    y=history_df["MSE Loss"],
    mode="lines+markers",
    name="MSE Loss"
))

loss_fig.update_layout(
    xaxis_title="Iterations",
    yaxis_title="Mean Squared Error",
    template="plotly_white"
)

st.plotly_chart(loss_fig, use_container_width=True)

# --------------------------------------------------
# 8. OBSERVATION TABLE
# --------------------------------------------------

st.divider()
st.subheader("6. Iteration-wise Observations")

st.dataframe(
    history_df.style.format({
        "Slope": "{:.5f}",
        "Intercept": "{:.5f}",
        "MSE Loss": "{:.5f}"
    }),
    use_container_width=True
)

csv_data = history_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download Observation Report (CSV)",
    data=csv_data,
    file_name="gradient_descent_observations.csv",
    mime="text/csv"
)

# --------------------------------------------------
# 9. LEARNING RATE COMPARISON
# --------------------------------------------------

st.divider()
st.subheader("7. Learning Rate Comparison")

if st.button("Compare Learning Rates"):
    comparison_rates = [0.0005, 0.001, 0.005, 0.01, 0.05]
    comparison_results = []

    n = len(X)

    for rate in comparison_rates:
        cm = float(initial_m)
        cb = float(initial_b)
        initial_loss = calculate_loss(cm, cb, X, y)
        final_loss = initial_loss
        status = "Converged / Stable"

        for _ in range(max_iterations):
            error = cm * X + cb - y

            dm = (2 / n) * np.sum(error * X)
            db = (2 / n) * np.sum(error)

            new_m = cm - rate * dm
            new_b = cb - rate * db

            if not np.isfinite(new_m) or not np.isfinite(new_b):
                status = "Diverged"
                break

            new_loss = calculate_loss(new_m, new_b, X, y)

            if not np.isfinite(new_loss) or new_loss > 1e15:
                status = "Diverged"
                break

            cm, cb = new_m, new_b
            final_loss = new_loss

        comparison_results.append({
            "Learning Rate": rate,
            "Initial Loss": initial_loss,
            "Final Loss": final_loss,
            "Slope": cm,
            "Intercept": cb,
            "Status": status
        })

    comparison_df = pd.DataFrame(comparison_results)

    st.dataframe(
        comparison_df.style.format({
            "Initial Loss": "{:.4f}",
            "Final Loss": "{:.4f}",
            "Slope": "{:.4f}",
            "Intercept": "{:.4f}"
        }),
        use_container_width=True
    )

    stable_results = comparison_df[
        comparison_df["Status"] == "Converged / Stable"
    ]

    if not stable_results.empty:
        best = stable_results.loc[
            stable_results["Final Loss"].idxmin()
        ]

        st.success(
            f"Lowest final loss: {best['Final Loss']:.5f} "
            f"at learning rate {best['Learning Rate']}."
        )

st.divider()
st.caption("Gradient Descent Virtual Lab | Machine Learning")

