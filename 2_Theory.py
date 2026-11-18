
import streamlit as st

st.set_page_config(page_title="Theory | Gradient Descent Lab", page_icon="📖", layout="wide")

st.title("📖 Theory")
st.caption("Understanding the Gradient Descent Algorithm")
st.divider()

st.subheader("1. What is Gradient Descent?")

st.write("""
Gradient Descent is an optimization algorithm used in Machine
Learning to minimize a cost or loss function. It works by
repeatedly adjusting model parameters in the direction that
reduces the value of the cost function.
""")

st.subheader("2. Working Principle")

st.write("""
The algorithm calculates the gradient (derivative) of the cost
function with respect to the model parameters. It then updates
these parameters in the opposite direction of the gradient.
This process continues until the algorithm converges or reaches
the maximum number of iterations.
""")

st.subheader("3. Mathematical Formula")

st.latex(r"\theta_{new} = \theta_{old} - \alpha \frac{dJ(\theta)}{d\theta}")

st.write("""
Where:

- θ = Model parameter
- α = Learning rate
- J(θ) = Cost function
- dJ(θ)/dθ = Gradient or derivative of the cost function
""")

st.subheader("4. Cost Function")

st.write("""
For Linear Regression, Mean Squared Error (MSE) is commonly
used as the cost function. It measures the average squared
difference between actual and predicted values.
""")

st.latex(r"J(m,b) = \frac{1}{n}\sum_{i=1}^{n}(y_i-(mx_i+b))^2")

st.write("""
Here, m represents the slope, b represents the intercept,
and n represents the total number of observations.
""")

st.subheader("5. Learning Rate")

st.write("""
The learning rate controls the size of each parameter update.

- Small learning rate: Slow convergence.
- Appropriate learning rate: Stable convergence.
- Large learning rate: May overshoot the minimum and fail to converge.
""")

st.subheader("6. Types of Gradient Descent")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("**Batch Gradient Descent**\n\nUses the entire training dataset for each update.")

with col2:
    st.info("**Stochastic Gradient Descent**\n\nUses one training example for each update.")

with col3:
    st.info("**Mini-Batch Gradient Descent**\n\nUses a small batch of training examples for each update.")

st.subheader("7. Applications")

st.markdown("""
- Linear Regression
- Logistic Regression
- Neural Networks
- Deep Learning
- Machine Learning model optimization
""")

st.divider()

if st.button("← Back to Aim"):
    st.switch_page("pages/1_Aim.py")

if st.button("Next: Procedure →"):
    st.switch_page("pages/3_Procedure.py")
