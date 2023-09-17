import streamlit as st

st.title("การทดสอบการเขียน Website ด้วย Streamlit")
col1, col2 = st.columns(2)
#col1.write("Col1")
#col2.write("Col2")
with col1:
    st.header("Prakit Junkhum")
with col2:
    st.image('./pic/123456.jpg')

st.header("Prakit Junkhum")
st.subheader("My Streamlit 01")

st.image('./pic/123456.jpg')