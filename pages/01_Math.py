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
---
# Interpretations
π (pronounced "pi") is a mathematical constant that represents the 
ratio of the circumference C of a circle to its diameter d. 
$$
π = {C \over a}
$$
The ratio $$C/d$$ is constant, regardless of the circles's size. For example if 
a circle has twice the diameter of another, it will also have twice the 
circumference, preserving the ratio $$C/d$$.                    

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
One such definition, due to Richard Baltzer and popularized by Edmund Landau, is 
the following: π is twice the smallest positive number at which the cosine function 
equals 0. π is also the smallest positive number at which the sine function equals 
zero, and the difference between consecutive zeroes of the sine function. The cosine 
can be defined independently of geometry as a power series, or as the solution of a 
differential equation. In similar spirit π can be defined using properties of the 
complex exponential, exp $$z$$, of a complex variable $$z$$. Like the cosine, the 
complex exponential can be defined in one of several ways. The set of complex numbers 
at which exp $$z$$ is equal to one is then an (imaginary) arythmetic progression of 
the form:
$$
\{..., -2πi, 0, 2πi, 4πi, ...\} = \{2πki | k ∈ ℤ\}
$$
and there is an unique positve real number π with this property.

A variation on the same idea, making use of sophisticated mathematical concepts of 
topology and algebra, is the following theorem: there is a unique (up to automorphism)
continuous isomorphism from the group R/Z of real numbers under addition modulo integers
(the circle group), onto the multiplicative group of complex numbers of absolute value 
one. The number π is then defined as half the magnitude of the deritive of this hmomorphism.

## Approximations

""", unsafe_allow_html=True)

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

render_footer()