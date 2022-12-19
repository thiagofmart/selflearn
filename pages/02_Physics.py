import streamlit as st
from streamlit.runtime.scriptrunner import add_script_run_ctx
from utils import load, create_image, generate_motion_df, update_motion_df, render_footer
from time import sleep
import asyncio
from threading import Thread
import streamlit.components.v1 as components
import json


frame = 64 # frame per second
max_velocity = 4
size_of_entities = 10
plane_dim = (736, 500)
if "rendered_images" not in st.session_state:
    st.session_state['rendered_images'] = []
    st.session_state['df_entities'] = generate_motion_df(size_of_entities, plane_dim, max_velocity)
    st.session_state['loop'] = True

placeholder = st.empty()
checkbox = st.checkbox('show entities')

circles=""
for row in st.session_state["df_entities"].iterrows():
    c = row[1]
    circles+=f'<circle id="ent-{row[0]}" class="entitie" cx="{((c.x/plane_dim[0])*100):.3f}%"  cy="{((c.y/plane_dim[1])*100):.3f}%" r="{((c.r/plane_dim[0]*100)):.3f}" \
stroke="black" stroke-width="0.15" fill="{"blue" if row[0]!=0 else "red"}" vi="{((c.vi/plane_dim[0]*100)):.3f}" vj="{((c.vj/plane_dim[0])*100):.3f}"/>\n'
javascript_string = load("javascript/motion.js")
javascript = f"""<script language="javascript">{javascript_string}</script>"""
print(javascript)
components.html(f"""
<svg id="board" width="100%" height="100%" viewBox="0 0 100 {(500/736*100)}" onmouseover="setInterval(() => {'{startProcessing(this)}'}, 1000)">
    <rect width="100%" height="100%" fill="white" stroke="red" stroke-width="0.1"/>
    {circles}
</svg>


<button onclick="updateMotion(document.getElementById('ent-0'))">UpdateMotion 0</button>
"""+javascript, height=plane_dim[1]+8)






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





render_footer()