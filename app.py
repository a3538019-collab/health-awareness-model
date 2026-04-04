import streamlit as st
import matplotlib.pyplot as plt

st.title("Health Awareness Video Spread Model")

st.write("This model shows how a health awareness video spreads among students")

# Inputs
initial_viewers = st.slider("Initial Viewers", 10, 1000, 100)
share_rate = st.slider("Share Rate (0-1)", 0.0, 1.0, 0.3)
decay = st.slider("Decay Rate (0-1)", 0.0, 1.0, 0.1)
days = st.slider("Days", 1, 30, 10)

# Simulation
reach = [initial_viewers]

for i in range(days):
    new_reach = reach[-1] + (share_rate * reach[-1]) - (decay * reach[-1])
    reach.append(new_reach)

# Output
st.subheader("Total Reach")
st.write(f"{int(reach[-1])} viewers")

# Graph
st.subheader("Spread Over Time")
fig, ax = plt.subplots()
ax.plot(reach)
ax.set_xlabel("Days")
ax.set_ylabel("Viewers")
st.pyplot(fig)
