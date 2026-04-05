import streamlit as st
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Viral Health Model", layout="wide")

# Custom CSS (Dark Theme + Glow)
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
h1, h2, h3 {
    color: #00ffd5;
    text-align: center;
}
.stSlider label {
    color: #ffffff !important;
}
.block-container {
    padding-top: 2rem;
}
.metric-box {
    background: linear-gradient(135deg, #1f1f2e, #2c2c3e);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 0px 15px rgba(0,255,213,0.2);
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("# 🌐 Viral Health Awareness Model")
st.markdown("### 🚀 Real-life Video Spread Simulation")

# Layout
col1, col2, col3 = st.columns(3)

with col1:
    initial_viewers = st.slider("👥 Initial Viewers", 10, 500, 50)

with col2:
    share_rate = st.slider("📤 Share Probability", 0.0, 1.0, 0.4)

with col3:
    connections = st.slider("🤝 Avg Friends", 1, 10, 3)

col4, col5 = st.columns(2)

with col4:
    decay = st.slider("📉 Interest Decay", 0.0, 1.0, 0.1)

with col5:
    days = st.slider("📅 Days", 1, 20, 10)

# Simulation
viewers = [initial_viewers]

for i in range(days):
    current = viewers[-1]
    new_viewers = current * share_rate * connections
    lost = current * decay
    next_viewers = current + new_viewers - lost
    viewers.append(next_viewers)

# Results Section
st.markdown("## 📊 Results Overview")

col6, col7, col8 = st.columns(3)

with col6:
    st.metric("📈 Total Reach", int(viewers[-1]))

with col7:
    st.metric("🔥 Growth", int(viewers[-1] - initial_viewers))

with col8:
    st.metric("📊 Avg Daily Increase", int((viewers[-1] - initial_viewers)/days))

# Graph
st.markdown("## 📉 Viral Spread Curve")

fig, ax = plt.subplots()
ax.plot(viewers, marker='o')
ax.set_facecolor("#0e1117")
fig.patch.set_facecolor("#0e1117")

ax.set_xlabel("Days", color="white")
ax.set_ylabel("People Reached", color="white")
ax.tick_params(colors='white')

st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("✨ Made with ❤️ for Health Awareness Project")
