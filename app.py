import streamlit as st

params = st.experimental_get_query_params()
url = params["url"]
st.write(url)
