import streamlit as st

st.title("การทดสอบการเขียน Website ด้วย Streamlit")
col1, col2 = st.columns(2)
#col1.write("Col1")
#col2.write("Col2")
with col1:
    st.image('./pic/123456.jpg')
with col2:
    st.header("คุณประกฤต จันทร์ขำ")
    st.text("บริษัท ไทยคอนโทรลโซลูชั่น จำกัด")
    st.write("กาญจนบุรี")
    st.markdown("มหาวิทยาลัยราชภัฏนครปฐม")
    
html_1 = """
<div style="background-color:#EC7063;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>Mr.Prakit Junkhum</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)

st.header("Prakit Junkhum")
st.subheader("My Streamlit 01")

st.image('./pic/123456.jpg')