
import streamlit as st

st.set_page_config(
    page_title="Gradient Descent Virtual Lab",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background-color: #f4f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.hero {
    background: linear-gradient(120deg, #123b70, #2878b9);
    padding: 45px 40px;
    border-radius: 16px;
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-size: 38px;
    margin-bottom: 10px;
}

.hero p {
    color: #e4efff;
    font-size: 17px;
}

.section-title {
    color: #173d68;
    font-size: 25px;
    font-weight: 700;
    margin-top: 25px;
}

.info-card {
    background: white;
    padding: 22px;
    border-radius: 12px;
    border: 1px solid #e1e8f0;
    min-height: 150px;
}

.info-card h3 {
    color: #174879;
    font-size: 19px;
}

.info-card p {
    color: #536477;
    font-size: 14px;
}

.stButton > button {
    background-color: #1769aa;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px 25px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #104c80;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("📊 ML Virtual Lab")
    st.caption("Machine Learning Laboratory")
    st.divider()

    st.markdown("### Experiment Navigation")
    st.markdown("""
    - 🏠 Home
    - 🎯 Aim
    - 📖 Theory
    - 📝 Procedure
    - 🧪 Simulation
    - 📈 Observations
    - ✅ Result
    - ❓ Pretest
    - 📝 Posttest
    - 📚 References
    """)

    st.divider()
    st.caption("Experiment 01")
    st.caption("Gradient Descent Algorithm")

# Main Hero Section
st.markdown("""
<div class="hero">
    <h1>Gradient Descent Virtual Lab</h1>
    <p>
        An Interactive Virtual Laboratory for Understanding
        Gradient Descent Algorithm in Machine Learning.
    </p>
    <p>
        Learn • Experiment • Simulate • Analyse
    </p>
</div>
""", unsafe_allow_html=True)

# Welcome
st.markdown('<div class="section-title">Welcome to the Virtual Lab</div>',
            unsafe_allow_html=True)

st.write("""
Welcome to the Machine Learning Virtual Laboratory.
This experiment helps students understand how the Gradient
Descent Algorithm works through interactive simulations,
visualizations and practical experimentation.
""")

# Experiment Information
st.markdown('<div class="section-title">Experiment Overview</div>',
            unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>🎯 Objective</h3>
        <p>Understand how Gradient Descent minimizes the
        cost function and optimizes model parameters.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>🧠 Concept</h3>
        <p>Learn about learning rate, derivatives,
        loss functions and parameter updates.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <h3>🧪 Simulation</h3>
        <p>Perform experiments by changing parameters
        and observing the optimization process.</p>
    </div>
    """, unsafe_allow_html=True)

# Learning Objectives
st.markdown('<div class="section-title">Learning Objectives</div>',
            unsafe_allow_html=True)

st.markdown("""
By completing this experiment, students will be able to:

1. Understand the basic concept of Gradient Descent.
2. Explain the role of derivatives in optimization.
3. Understand the effect of learning rate.
4. Observe how model parameters are updated.
5. Analyse the reduction of loss over iterations.
6. Understand how Gradient Descent helps find the best-fit line.
""")

# Experiment Details
st.markdown('<div class="section-title">Experiment Details</div>',
            unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.info("**Experiment Name:** Gradient Descent Algorithm")

with col2:
    st.info("**Subject:** Machine Learning")

# Start Button
st.divider()

st.markdown("### Ready to begin your experiment?")

if st.button("Start Experiment →"):
    st.switch_page("pages/1_Aim.py")

st.caption("Machine Learning Virtual Lab | Continuous Assessment")
