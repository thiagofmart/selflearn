import streamlit as st
from utils import render_footer


posts = ["Business Intelligence", "KPIs"]
st.markdown("""
# Economy and Finance Page
---

Here you can see some posts about economy and finance:

"""
)
data, dbms = st.tabs(posts)
st.markdown("""
# There is no content already 😔
""")

render_footer()