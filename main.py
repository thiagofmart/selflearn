import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from utils import get_sin_df, generate_motion_df, update_motion_df
from time import sleep
from PIL import Image, ImageDraw






placeholder = st.empty()
if st.checkbox('show entities'):
    frame = 128 #10 frame per second
    max_velocity = 7.5
    size_of_entities = 15
    plane_dim = (800, 500)
    df_entities = generate_motion_df(size_of_entities, plane_dim, max_velocity)
    with placeholder.container():
        #for i in range(0, 100):
        while True:
            sleep(1/frame)
            image = Image.new('RGBA', (plane_dim[0]+1, plane_dim[1]+1))
            draw = ImageDraw.Draw(image)
            #board
            draw.rectangle([(0,0), (plane_dim[0],plane_dim[1])], fill="white", outline="red", width=1)
            for row in df_entities.iterrows():
                x, y, r = row[1]["x"], row[1]["y"], row[1]["r"]
                draw.ellipse(
                    [ #defining coordinates of
                        (x-r, y-r), # x0, y0
                        (x+r, y+r) # x1, y1
                    ], # where x0 <= x1 and y0 <= y1
                    fill = 'blue', 
                    outline ='blue'
                )
            placeholder.image(image)
            df_entities = update_motion_df(df_entities, plane_dim, frame)




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


