import streamlit as st
import matplotlib.pyplot as plt

st.title("Health Awareness Video Viral Spread Model")

st.write("Simulating real-life sharing of a video among students")

# Inputs
initial_viewers = st.slider("Initial Viewers", 10, 500, 50)
share_rate = st.slider("Share Probability (0-1)", 0.0, 1.0, 0.4)
connections = st.slider("Avg Friends per Student", 1, 10, 3)
decay = st.slider("Interest Decay (0-1)", 0.0, 1.0, 0.1)
days = st.slider("Days", 1, 20, 10)

# Simulation
viewers = [initial_viewers]

for i in range(days):
    current = viewers[-1]
    
    # Network spread
    new_viewers = current * share_rate * connections
    
    # Decay (people losing interest)
    lost = current * decay
    
    next_viewers = current + new_viewers - lost
    viewers.append(next_viewers)

# Output
st.subheader("Total Reach")
st.write(f"{int(viewers[-1])} people reached")

# Graph
st.subheader("Viral Spread Over Time")
fig, ax = plt.subplots()
ax.plot(viewers)
ax.set_xlabel("Days")
ax.set_ylabel("People Reached")
st.pyplot(fig)

