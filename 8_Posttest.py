
import streamlit as st

st.set_page_config(page_title="Posttest", page_icon="📝", layout="wide")

st.title("📝 Posttest")
st.write("Evaluate your understanding after completing the experiment.")
st.divider()

questions = [
    {
        "q": "1. Gradient Descent updates parameters in which direction?",
        "options": [
            "Direction of increasing cost",
            "Opposite direction of the gradient",
            "Random direction",
            "No direction"
        ],
        "answer": "Opposite direction of the gradient"
    },
    {
        "q": "2. What happens when the learning rate is very small?",
        "options": [
            "Slow convergence",
            "Immediate convergence",
            "Infinite dataset",
            "Automatic classification"
        ],
        "answer": "Slow convergence"
    },
    {
        "q": "3. What does MSE measure?",
        "options": [
            "Average squared prediction error",
            "Number of features",
            "Dataset size",
            "Number of clusters"
        ],
        "answer": "Average squared prediction error"
    },
    {
        "q": "4. What is an iteration in Gradient Descent?",
        "options": [
            "One complete parameter update",
            "Deleting the model",
            "Loading a dataset",
            "Creating a graph"
        ],
        "answer": "One complete parameter update"
    },
    {
        "q": "5. What indicates successful convergence?",
        "options": [
            "Increasing loss",
            "Stable or minimized loss",
            "Increasing dataset size",
            "Random parameter values"
        ],
        "answer": "Stable or minimized loss"
    }
]

with st.form("posttest"):
    answers = []

    for i, question in enumerate(questions):
        st.markdown(f"**{question['q']}**")
        answers.append(
            st.radio(
                "Choose your answer:",
                question["options"],
                key=f"post_{i}"
            )
        )

    submitted = st.form_submit_button("Submit Posttest")

if submitted:
    score = sum(
        answers[i] == questions[i]["answer"]
        for i in range(len(questions))
    )

    st.metric("Your Score", f"{score}/5")

    if score >= 4:
        st.success("Excellent! You have understood the experiment.")
    elif score >= 2:
        st.info("Good effort! Revise the concepts for improvement.")
    else:
        st.warning("Please revisit the theory and simulation sections.")
