import streamlit as st
import streamlit.components.v1 as components
from utils import load

st.set_page_config(
    page_title="self learn",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)



variables = {
    "github": "https://github.com/thiagofmart",
    "linkedin": "https://www.linkedin.com/in/thiago-ferreira-martins-45004b191/",
    "instagram": "https://www.instagram.com/thiago_fmart/",
    "email": "thiago.fmartins@outlook.com",
    "link_style":'color:white; text-decoration: none; margin-left:20px; margin-right:20px;',
}

javascript = f'<script language="javascript">{load("javascript/index.js")}</script>'

st.markdown("""
# Thiago Martins
---""")
st.markdown("""
<div style="display: flex; justify-content: center; ">
<img src="https://avatars.githubusercontent.com/u/71234183?v=4"
    style="\
        padding:1px;\
        width: 30%;\
        max-width: 250px;\
        border-radius: 100%;\
        background: linear-gradient(45deg, rgb(255, 75, 75), rgb(255, 253, 128));\
    ">
</div>

---

Welcome to my self learn studio, the place where I post anything that I want and when I want... Hope you enjoy some randoom content. 😅

The goal of this kind of blog is to be a location where I can make the most datailed explanation about math, tecnologies, physics and economy subjects that I'm currently studying...
I'm not the owner of the truth and this is not any kind of recommendation of anything that you would see here. 
""",
unsafe_allow_html=True)

st.markdown("""
Hello There... :smile:

    def fibonacci(number):
        if number <= 1:
            return number
        else:
            return fibonacci(number - 1) + fibonacci(number - 2)
---

$$
ax^2 + bx + c = 0
$$ 
""")

components.html(javascript+load("html/myFooter.html").format(
    github=variables["github"],
    linkedin=variables["linkedin"],
    instagram=variables["instagram"],
    email=variables["email"],
    link_style=variables["link_style"],
    )
)


