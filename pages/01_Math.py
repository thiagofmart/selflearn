import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from utils import get_sin_df, render_footer, file_selector


posts = ["π (PI) Analysis", "Sinusoidal Function"]
st.markdown("""
# Mathematical Page
---

Here you can see some posts about math:

"""
)
pi_analysis, sinusoidal_function = st.tabs(posts)
with pi_analysis:
    st.markdown("""
# π Analysis

π (pronounced "pi") is a mathematical constant that represents the 
ratio of the circumference C of a circle to its diameter d. 
$$
π = {C \over a}
$$
It is approximately equal to 3.14159, but it is an irrational number, which 
means that it cannot be expressed exactly as a decimal. The decimal 
representation of π goes on indefinitely. It is one of the most well-known
and widely used mathematical constants in the world and is essential in many
fields, including geometry, trigonometry, and engineering.

The ratio $$C/d$$ is constant, regardless of the circles's size. For example if 
a circle has twice the diameter of another, it will also have twice the 
circumference, preserving the ratio $$C/d$$.                    

<img src="assets/giphy.gif" width="100" height="100" />

This definition of π implicitly 
makes use of flat (Euclidian) geometry; although the notion of a circle  can
be extended to any curve (non-Euclidean) geometry, these new circles will no
longer satisfy the formula $$π=C/d$$.

Here the circunmference of a circle is the arc length around the perimeter 
of the circle, a quantity which can be formally defined independently of 
geometry using limits - a concept in calculus. For example, one may directly 
compute the arc length of the top half of the unit circle, given in Cartesian 
coordinates by the equation $$x^2+y^2=1$$, as the integral:
$$
π = {\int_{-1}^1 {dx \over \sqrt{1-x^2}}}
$$


---""", unsafe_allow_html=True)

with sinusoidal_function:
    st.markdown("""
    # Sinusoidal Function
    """)
    frequency = st.slider("F = Frequency", min_value=0.5, max_value=5.0, value=1.0)
    amplitude = st.slider("A = Amplitude", min_value=0.5, max_value=5.0, value=1.0)
    period = st.slider("P = Period", min_value=np.pi, max_value=5*np.pi, value=2*np.pi)
    hshift = st.slider("Hs = Horizontal Shift", min_value=-3.0, max_value=6.0, value=0.0)
    vshift = st.slider("Vs = Vertical Shift", min_value=-4.0, max_value=4.0, value=0.0)

    fig = px.line(
        get_sin_df(frequency, amplitude, period, hshift, vshift),
        title="x = [0, P]+ Hs <=> f(x) = A * sin( F * (x + Hs) ) + Vs",
        range_x=[-5*np.pi, 5*np.pi],
        range_y=[-5, 5]
    )

    st.plotly_chart(fig)


st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

render_footer()