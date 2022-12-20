import streamlit as st
from utils import load, create_image, generate_motion_df, update_motion_df, render_footer
from time import sleep
import asyncio
from threading import Thread
import streamlit.components.v1 as components


st.markdown("""
# Elastic collision

---

https://byjus.com/physics/elastic-collision/

---

""")

frame = 64 # frame per second
max_velocity = 5
size_of_entities = 10
plane_dim = (736, 500)
if "rendered_images" not in st.session_state:
    st.session_state['rendered_images'] = []
    st.session_state['df_entities'] = generate_motion_df(size_of_entities, plane_dim, max_velocity)
    st.session_state['loop'] = True

circles=""
for row in st.session_state["df_entities"].iterrows():
    c = row[1]
    circles+=f'<circle id="ent-{row[0]}" class="entitie" cx="{((c.x/plane_dim[0])*100):.3f}%"  cy="{((c.y/plane_dim[1])*100):.3f}%" r="{((c.r/plane_dim[0]*100)):.3f}%" \
stroke="black" stroke-width="0.15" fill="{"blue" if row[0]!=0 else "red"}" vi="{((c.vi/plane_dim[0]*100)):.3f}%" vj="{((c.vj/plane_dim[0])*100):.3f}%"/>\n'
c = st.session_state["df_entities"].loc[0, :]

main_circle = f''
print(main_circle)
javascript_string = load("javascript/motion.js")
javascript = f"""<script language="javascript">{javascript_string}</script>"""
components.html(f"""
<svg id="board" width="100%" height="100%" viewBox="0 0 100 {(plane_dim[1]/plane_dim[0]*100)}" onmouseover="startProcessing(this)" onmouseleave="stopProcessing()">
    <rect width="100%" height="100%" fill="rgba(38,39,48,0.5)" stroke="linear-gradient(45deg, rgb(255, 75, 75), rgb(255, 253, 128))" stroke-width="0.1"/>
    {circles}
</svg>
<br>

<div width="70%" style="display: flex; justify-content:center;">
    <svg id="analysis" width="120px" height="120px" style="float: left;">
        <rect width="100%" height="100%" fill="rgba(38,39,48,0.5)" stroke="linear-gradient(45deg, rgb(255, 75, 75), rgb(255, 253, 128))" stroke-width="0.1"/>
        <circle id="main-circle" cx="50%"  cy="50%" r="{((c.r/plane_dim[0]*500)):.3f}%" stroke="black" 
        stroke-width="0.15" fill="red" vi="{((c.vi/plane_dim[0]*400)):.3f}%" vj="{((c.vj/plane_dim[0])*400):.3f}%"/>
        <defs>
            <marker id="arrowhead" markerWidth="10" markerHeight="8" 
            refX="0" refY="3.5" orient="auto", fill="#5f5f5f">
            <polygon points="0 0, 10 3.5, 0 7" />
            </marker>
        </defs>
        <line id="arrow" x1="50%" y1="50%" x2="{50+((c.vi/plane_dim[0])*400):.3f}%" y2="{50+((c.vj/plane_dim[0])*400):.3f}%" stroke="#5f5f5f" 
        stroke-width="1.4%" marker-end="url(#arrowhead)" />
    </svg>
    <div style="display: block; float: left; width: 200px; margin-left: 5px">
        <p id="vi-label" style="color: white;">Vi = {(c.vi/plane_dim[0])*100}</p>
        <p id="vj-label" style="color: white;">Vj = {(c.vj/plane_dim[0])*100}</p>
        <p id="coordinates" style="color: white;">Cordinates = ({(c.x/plane_dim[0])*100}, {(c.y/plane_dim[0])*100})</p>
    </div>
</div>
"""+javascript, height=plane_dim[1]+plane_dim[1]*+4)

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

render_footer()