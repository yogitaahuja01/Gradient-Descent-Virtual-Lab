
import streamlit as st

st.set_page_config(
    page_title="Procedure | Gradient Descent Lab",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Experimental Procedure")
st.caption("Step-by-step procedure for performing Gradient Descent")
st.divider()

st.subheader("Steps to Perform the Experiment")

steps = [
    ("Step 1: Open the Simulation",
     "Navigate to the Simulation section of the virtual laboratory."),

    ("Step 2: Select Dataset",
     "Choose the sample dataset or generate a dataset for Linear Regression."),

    ("Step 3: Set Initial Parameters",
     "Set the initial slope and intercept values of the regression model."),

    ("Step 4: Set Learning Rate",
     "Adjust the learning rate to control the size of parameter updates."),

    ("Step 5: Set Number of Iterations",
     "Specify the maximum number of iterations for the algorithm."),

    ("Step 6: Run Gradient Descent",
     "Execute the algorithm and observe how the slope and intercept change."),

    ("Step 7: Observe Results",
     "Study the loss function, regression line and convergence graph."),

    ("Step 8: Analyse",
     "Repeat the experiment using different learning rates and compare results.")
]

for title, description in steps:
    with st.expander(title, expanded=True):
        st.write(description)

st.subheader("Precautions")

st.markdown("""
- Select a suitable learning rate.
- Avoid excessively large learning rates.
- Use a sufficient number of iterations.
- Observe the loss function after each update.
- Reset the simulation before starting a new experiment.
""")

st.divider()

if st.button("Next: Simulation →"):
    st.switch_page("pages/4_Simulation.py")
