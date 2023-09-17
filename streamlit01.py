import streamlit as st

st.title("การทดสอบการเขียน Website ด้วย Streamlit")
col1, col2 = st.columns(2)
#col1.write("Col1")
#col2.write("Col2")
with col1:
    st.image('./pic/123456.jpg')
with col2:
    
    st.header("คุณประกฤต จันทร์ขำ")
    st.subheader("บริษัท ไทยคอนโทรลโซลูชั่น จำกัด")
    st.subheader("กาญจนบุรี")
    st.subheader("มหาวิทยาลัยราชภัฏนครปฐม")
    

st.header("Prakit Junkhum")
st.subheader("My Streamlit 01")

st.image('./pic/123456.jpg')