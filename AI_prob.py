import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


col1, col2 = st.columns(2)

with col1:
    m = st.slider("$\mu $", min_value=-10.0, max_value = 10.0)
with col2:
    sigma = st.slider("$\sigma $", 0.1, 10.0)

def gauss(x, m, s):
    return 1 / (s * (2 * np.pi)**0.5) * np.exp(- ((x - m)**2) / (2 * s**2))

def visualize():
    st.subheader("Gauss Mass Function")
    x = np.linspace(-10, 10, 1000)
   
    fig, ax = plt.subplots()
    ax.xlabel("x")
    ax.ylabel("P(x)")
    ax.plot(x, gauss(x, m = m, s = sigma))

    ax.axhline(0, color='green')
    ax.axvline(0, color='green')
    ax.legend()
    st.pyplot(fig)

visualize()