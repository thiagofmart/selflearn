import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from utils import get_sin_df
from time import sleep


placeholder = st.empty()




####################################################################
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
###############################################################################################
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')



"""
progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))

for i in range(1, 101):
    # Update progress bar.
    progress_bar.progress(i)

    new_rows = np.random.randn(10, 2)

    # Update status text.
    status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    sleep(0.1)

status_text.text('Done!')
st.balloons()
"""


max_force = 20
size_of_entities = 15
force_vectors = np.random.uniform(0, max_force, size_of_entities*2) # generate x and y forces vector based on max_force
df_entities = pd.DataFrame({
    "x":np.ceil(np.random.rand(size_of_entities)*30), #x coordinate between [0-30]
    "y":np.ceil(np.random.rand(size_of_entities)*30), #y coordinate between [0-30]
    "r":np.concatenate(([20], np.random.rand(size_of_entities-1)*25), ), #radius between [0-1]
    'vi':force_vectors[0:size_of_entities], # divide the vector into two and gets the first part
    "vj":force_vectors[size_of_entities:], # divide the vector into two and gets the second part
})

if st.checkbox('show entities'):
    with placeholder.container():
        for i in range(0, 10):
            sleep(0.5)
            force_vectors = np.random.uniform(0, max_force, size_of_entities*2) # generate x and y forces vector based on max_force
            df_entities = pd.DataFrame({
                "x":np.ceil(np.random.rand(size_of_entities)*30), #x coordinate between [0-30]
                "y":np.ceil(np.random.rand(size_of_entities)*30), #y coordinate between [0-30]
                "r":np.concatenate(([20], np.random.rand(size_of_entities-1)*25), ), #radius between [0-1]
                'vi':force_vectors[0:size_of_entities], # divide the vector into two and gets the first part
                "vj":force_vectors[size_of_entities:], # divide the vector into two and gets the second part
            })
            fig = go.Figure(data=go.Scatter(
                x = df_entities["x"],
                y = df_entities["y"],
                mode="markers",
                marker={
                    "size": df_entities["r"],
                    "color": [0] + [1 for i in range(1,size_of_entities)],
                }
            ))
            placeholder.plotly_chart(fig)
