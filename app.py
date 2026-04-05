import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.subheader("Spread Over Time")

days_list = list(range(len(viewers)))

fig, ax = plt.subplots()

ax.plot(days_list, viewers, marker='o', linestyle='-', label="Total Viewers")

ax.set_xlabel("Days")
ax.set_ylabel("People Reached")
ax.set_title("Health Awareness Video Spread")

ax.legend()
ax.grid(True)

st.pyplot(fig)
