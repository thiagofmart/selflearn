import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit.runtime.scriptrunner import add_script_run_ctx
import streamlit.components.v1 as components
from utils import create_image, get_sin_df, generate_motion_df, update_motion_df
from time import sleep
import asyncio
from threading import Thread


frame = 64 # frame per second
max_velocity = 4
size_of_entities = 10
plane_dim = (800, 500)
if "rendered_images" not in st.session_state:
    st.session_state['rendered_images'] = []
    st.session_state['df_entities'] = generate_motion_df(size_of_entities, plane_dim, max_velocity)
    st.session_state['loop'] = True

placeholder = st.empty()
checkbox = st.checkbox('show entities')

async def render_images(plane_dim):
    while True:
        if not st.session_state.loop:
            break
        if len(st.session_state.rendered_images) < 10:
            while (len(st.session_state.rendered_images) < 250):
                if not st.session_state.loop:
                    break
                st.session_state.df_entities = await update_motion_df(st.session_state.df_entities, plane_dim)
                image = await create_image(plane_dim, st.session_state.df_entities)
                st.session_state.rendered_images.append(image)
                print(f"rendering {len(st.session_state.rendered_images)}")

async def display_images(frame):
    while True:
        sleep(1/frame)
        if not st.session_state.loop:
            break
        if st.session_state.rendered_images:
            placeholder.image(st.session_state.rendered_images.pop(0))
       


if checkbox:
    with placeholder.container():
        st.session_state.loop = True
        t1 = Thread(target=lambda x: asyncio.run(render_images(x)), args=(plane_dim,))
        add_script_run_ctx(t1)
        t1.start()
        asyncio.run(display_images(frame))
if not checkbox:
    st.session_state.loop = False



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


