import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from utils import create_image, get_sin_df, generate_motion_df, update_motion_df
from time import sleep
import asyncio


placeholder = st.empty()
checkbox = st.checkbox('show entities')
async def display_images(frame):
    global df_entities, plane_dim
    while True:
        for i in range(0, 1_000):
            df_entities = await update_motion_df(df_entities, plane_dim)
            image = await create_image(plane_dim, df_entities)
            sleep(1/frame)
            placeholder.image(image)

if checkbox:
    frame = 10 # frame per second
    max_velocity = 7.5
    size_of_entities = 10
    plane_dim = (800, 500)
    df_entities = generate_motion_df(size_of_entities, plane_dim, max_velocity)    
    with placeholder.container():
        asyncio.run(display_images(frame))


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


