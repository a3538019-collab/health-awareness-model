import streamlit as st

st.title("Health Awareness Model")

st.write("This model shows how awareness impacts health risk")

awareness = st.slider("Awareness Level (0-100)", 0, 100, 50)
exercise = st.slider("Exercise (hours/week)", 0, 10, 3)
diet = st.slider("Diet Quality (1-10)", 1, 10, 5)

risk = 100 - (0.4 * awareness + 0.3 * exercise * 5 + 0.3 * diet * 10)

st.subheader("Health Risk Score")
st.write(f"{risk:.2f} %")

if risk < 30:
    st.success("Low Risk")
elif risk < 60:
    st.warning("Moderate Risk")
else:
    st.error("High Risk")
