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
ax.plot(days_list, viewers, marker='o')

ax.set_xlabel("Days")
ax.set_ylabel("People Reached")
ax.set_title("Video Spread Over Time")

ax.grid(True)

st.pyplot(fig)

# -------- GRAPH 2 --------
st.subheader("Daily Growth")

growth_list = np.diff(viewers)

fig2, ax2 = plt.subplots()
ax2.plot(growth_list, marker='o')

ax2.set_xlabel("Days")
ax2.set_ylabel("New Viewers")
ax2.set_title("Daily Increase in Viewers")

ax2.grid(True)

st.pyplot(fig2)

# -------- AUTO EXPLANATION --------
st.subheader("Analysis of Result")

growth = viewers[-1] - initial_viewers

if share_rate > 0.7 and decay < 0.2:
    st.success("The video is spreading very fast. High sharing and low decay are creating a viral effect.")

elif share_rate < 0.3:
    st.warning("The video spread is slow because fewer people are sharing it.")

elif decay > 0.4:
    st.error("High decay rate is reducing the spread. People are losing interest quickly.")

else:
    st.info("The video is spreading at a moderate rate with balanced sharing and decay.")

# Extra info
st.write(f"Final Reach: {int(viewers[-1])} people")
st.write(f"Total Growth: {int(growth)} people added")
