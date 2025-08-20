import streamlit as st
from numpy.distutils.system_info import language_map
from streamlit import markdown

st.sidebar.markdown("clicked page1")
st.sidebar.markdown("Side Menu")
st.sidebar.button("Click")
st.sidebar.radio("성별", ["여자","남자"])
#page
st.title("page1")
st.markdown("Mark Down")
st.header("header")
st.subheader("subheader")
st.caption("caption")
st.code("""
 def func():
 print("OK")
 def func2():
 print("OK2")
 
 
 """,language="python")