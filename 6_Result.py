
import streamlit as st

st.set_page_config(page_title="Result", page_icon="✅", layout="wide")

st.title("✅ Result")
st.caption("Conclusion of the Gradient Descent Experiment")
st.divider()

st.subheader("Experimental Result")

st.write("""
The Gradient Descent Algorithm was studied and implemented
for Linear Regression using a sample dataset.
""")

st.write("""
The algorithm iteratively updated the slope and intercept
parameters by calculating the gradients of the Mean Squared
Error cost function.
""")

st.write("""
The simulation demonstrated how the learning rate and
number of iterations influence the optimization process.
""")

st.subheader("Key Findings")

findings = [
    "Gradient Descent minimizes the cost function through iterative parameter updates.",
    "The learning rate controls the step size during optimization.",
    "A suitable learning rate helps achieve stable convergence.",
    "The loss function generally decreases as the model parameters improve.",
    "Gradient Descent is useful for optimizing Machine Learning models."
]

for i, finding in enumerate(findings, 1):
    st.markdown(f"**{i}.** {finding}")

st.success("""
Conclusion: The Gradient Descent Algorithm was successfully
implemented and its optimization behaviour was studied through
an interactive simulation.
""")

st.divider()

if st.button("Go to Simulation"):
    st.switch_page("pages/4_Simulation.py")
