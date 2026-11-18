
import streamlit as st

st.set_page_config(page_title="Pretest", page_icon="❓", layout="wide")

st.title("❓ Pretest")
st.write("Test your basic knowledge before performing the experiment.")
st.divider()

questions = [
    {
        "q": "1. What is the main purpose of Gradient Descent?",
        "options": [
            "Increase the dataset size",
            "Minimize the cost function",
            "Remove all features",
            "Generate random values"
        ],
        "answer": "Minimize the cost function"
    },
    {
        "q": "2. What does the learning rate control?",
        "options": [
            "Dataset size",
            "Number of features",
            "Step size of parameter updates",
            "Number of classes"
        ],
        "answer": "Step size of parameter updates"
    },
    {
        "q": "3. Which mathematical quantity guides parameter updates?",
        "options": [
            "Gradient",
            "Median",
            "Mode",
            "Variance"
        ],
        "answer": "Gradient"
    },
    {
        "q": "4. What happens when the learning rate is too large?",
        "options": [
            "Always faster convergence",
            "The algorithm may overshoot the minimum",
            "The dataset disappears",
            "Loss becomes zero immediately"
        ],
        "answer": "The algorithm may overshoot the minimum"
    },
    {
        "q": "5. Which loss function is commonly used in Linear Regression?",
        "options": [
            "Accuracy",
            "Mean Squared Error",
            "Silhouette Score",
            "Confusion Matrix"
        ],
        "answer": "Mean Squared Error"
    }
]

with st.form("pretest"):
    answers = []

    for i, question in enumerate(questions):
        st.markdown(f"**{question['q']}**")
        answers.append(
            st.radio(
                "Choose your answer:",
                question["options"],
                key=f"pre_{i}"
            )
        )

    submitted = st.form_submit_button("Submit Pretest")

if submitted:
    score = sum(
        answers[i] == questions[i]["answer"]
        for i in range(len(questions))
    )

    st.metric("Your Score", f"{score}/5")

    if score >= 4:
        st.success("Excellent! You have a good basic understanding.")
    elif score >= 2:
        st.info("Good attempt! Review the theory before continuing.")
    else:
        st.warning("Please study the theory section before the simulation.")
