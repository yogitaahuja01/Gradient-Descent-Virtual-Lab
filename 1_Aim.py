
import streamlit as st

st.set_page_config(page_title="Aim | Gradient Descent Lab", page_icon="🎯", layout="wide")

st.title("🎯 Aim of the Experiment")
st.caption("Experiment 01 | Gradient Descent Algorithm")
st.divider()

st.subheader("Aim")

st.write("""
To implement and understand the Gradient Descent Algorithm
used in Machine Learning for minimizing a cost function and
optimizing model parameters through iterative updates.
""")

st.subheader("Objectives")

objectives = [
    "Understand the working principle of Gradient Descent.",
    "Study the role of learning rate in optimization.",
    "Understand how derivatives are used to update model parameters.",
    "Observe the reduction in cost function over multiple iterations.",
    "Analyse the effect of different learning rates on convergence.",
    "Determine the optimal parameters for a Linear Regression model."
]

for i, objective in enumerate(objectives, 1):
    st.markdown(f"**{i}.** {objective}")

st.subheader("Expected Learning Outcome")

st.success("""
After completing this experiment, students will be able to
implement Gradient Descent, interpret its convergence behaviour,
and understand how it minimizes the loss function.
""")

st.divider()

if st.button("Next: Theory →"):
    st.switch_page("pages/2_Theory.py")
