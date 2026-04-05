import streamlit as st
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Health Video Model", layout="centered")

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
h1 {
    color: #ff4b4b;
    text-align: center;
}
.stMetric {
    background-color: #ffffff;
    padding: 10px;
    border-radius: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("📺 Health Awareness Video Spread Model")

st.markdown("### 🚀 Simulating Viral Spread Among Students")

# Inputs in columns
col1, col2 = st.columns(2)

with col1:
    initial_viewers = st.slider("👥 Initial Viewers", 10, 500, 50)
    share_rate = st.slider("📤 Share Probability", 0.0, 1.0, 0.4)

with col2:
    connections = st.slider("🤝 Avg Friends", 1, 10, 3)
    decay = st.slider("📉 Interest Decay", 0.0, 1.0, 0.1)

days = st.slider("📅 Days", 1, 20, 10)

# Simulation
viewers = [initial_viewers]

for i in range(days):
    current = viewers[-1]
    new_viewers = current * share_rate * connections
    lost = current * decay
    next_viewers = current + new_viewers - lost
    viewers.append(next_viewers)

# Metrics
st.markdown("## 📊 Results")

col3, col4 = st.columns(2)

with col3:
    st.metric("📈 Total Reach", int(viewers[-1]))

with col4:
    growth = viewers[-1] - initial_viewers
    st.metric("🔥 Growth", int(growth))

# Graph
st.markdown("## 📉 Spread Over Time")

fig, ax = plt.subplots()
ax.plot(viewers, marker='o')
ax.set_xlabel("Days")
ax.set_ylabel("People Reached")
ax.set_title("Viral Growth Curve")

st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("✨ Developed for Health Awareness Modelling Project")

