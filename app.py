import streamlit as st
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Health Awareness Model", layout="centered")

# Title
st.title("Health Awareness Video Spread Model")

st.write("This model simulates how a health awareness video spreads among students through sharing.")

# Inputs
st.subheader("Input Parameters")

initial_viewers = st.slider("Initial Viewers", 10, 500, 50)
share_rate = st.slider("Share Probability", 0.0, 1.0, 0.4)
connections = st.slider("Average Friends", 1, 10, 3)
decay = st.slider("Interest Decay", 0.0, 1.0, 0.1)
days = st.slider("Days", 1, 20, 10)

# Simulation
viewers = [initial_viewers]

for i in range(days):
    current = viewers[-1]
    new_viewers = current * share_rate * connections
    lost = current * decay
    next_viewers = current + new_viewers - lost
    viewers.append(next_viewers)

# Results
st.subheader("Results")

st.metric("Total Reach", int(viewers[-1]))

# Graph
st.subheader("Spread Over Time")

fig, ax = plt.subplots()
ax.plot(viewers)
ax.set_xlabel("Days")
ax.set_ylabel("People Reached")

st.pyplot(fig)
