import streamlit as st
import pandas as pd

st.title("การทดสอบการเขียน Website ด้วย Streamlit")
st.header("Prakit Junkhum")
st.subheader("My Streamlit 01")

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
<div style="background-color:#77c900;padding:15px 15px 15px 15px;margin:30px 30px 30px 30px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>Mr.Prakit Junkhum</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)


colx1, colx2, colx3 = st.columns(3)
with colx1:
    st.markdown("<center><h5>Header 1</h5></center>", unsafe_allow_html=True)
    st.image('./pic/iris1.jpg')
with colx2:
    st.markdown("<center><h5>Header 2</h5></center>", unsafe_allow_html=True)
    st.image('./pic/iris2.jpg')
with colx3:
    st.markdown("<center><h5>Header 3</h5></center>", unsafe_allow_html=True)
    st.image('./pic/iris3.jpg')


dt = pd.read_csv('./data/iris.csv')
st.write(dt.head(10))

dt1 = dt['petal.length'].sum()
dt2 = dt['petal.width'].sum()
dt3 = dt['sepal.length'].sum()
dt4 = dt['sepal.width'].sum()

dx = [dt1, dt2, dt3, dt4]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4"])

if st.button("Show chart"):
    dt.bar_chart(dx2)
    st.button("Don't show chart")
else:
    st.button("Don't show chart")