
import streamlit as st

st.set_page_config(page_title="References", page_icon="📚", layout="wide")

st.title("📚 References and Learning Resources")
st.divider()

st.subheader("Books")

st.markdown("""
1. Tom M. Mitchell — *Machine Learning*.
2. Christopher M. Bishop — *Pattern Recognition and Machine Learning*.
3. Aurélien Géron — *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow*.
""")

st.subheader("Online Resources")

st.markdown("""
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
""")

st.subheader("Software and Libraries")

st.markdown("""
- Python
- Streamlit
- NumPy
- Pandas
- Plotly
- Scikit-learn
""")

st.success("References section completed.")
