import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title
st.title("Health Awareness Video Spread Model")

st.write("This model simulates how a health awareness video spreads among students.")

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

# Result
st.subheader("Results")

st.metric("Total Reach", int(viewers[-1]))

# -------- GRAPH 1 --------
st.subheader("Spread Over Time")

days_list = list(range(len(viewers)))

fig, ax = plt.subplots()
ax.plot(days_list, viewers, marker='o', linestyle='-')

ax.set_xlabel("Days")
ax.set_ylabel("People Reached")
ax.set_title("Video Spread Over Time")

ax.grid(True)

st.pyplot(fig)

# -------- GRAPH 2 --------
st.subheader("Daily Growth")

growth = np.diff(viewers)

fig2, ax2 = plt.subplots()
ax2.plot(growth, marker='o')

ax2.set_xlabel("Days")
ax2.set_ylabel("New Viewers")
ax2.set_title("Daily Increase in Viewers")

ax2.grid(True)

st.pyplot(fig2)
