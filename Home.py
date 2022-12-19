import streamlit as st
from utils import render_footer

st.set_page_config(
    page_title="self learn",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
    }
)





st.markdown("""# Thiago Martins
***
""")
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
Welcome to my self learn studio, the place where I post anything that I want and when I want... 
Hope you enjoy some randoom content. 😅

My name is Thiago Ferreira Martins, I'm a brazilian Jr programmer trying to go beyond of study pattern
made by colleges roadmap. My main programming languages are Python and JavaScript, but I'm also looking for 
more knowledge in C++, C, solidity and vyper programming languages.

The goal of this kind of blog is to be a location where I can make the most datailed explanation 
about math, tecnologies, physics and economy subjects that I'm currently studying... I'm not the 
owner of the truth and this is not any kind of recommendation of anything that you would see here. 
If you see something wrong or that you disagree you can contact me with by email or telegram wich
are in the footer of this webiste. I expect constructive criticism and not free hate
""",
unsafe_allow_html=True)

st.markdown("""
---
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
render_footer()


