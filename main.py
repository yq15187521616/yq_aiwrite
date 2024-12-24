import streamlit as st
from utils import generate_script

api_key=1
st.title("公文写作AI")
subject= st.text_input("--请输入文章主题")
genres= st.text_input("--请输入文章类型",value="工作总结")
number=st.number_input("--请输入文章字数",min_value=100,max_value=1000,value=500,step=100)
creativity=st.slider("文章的创造力(数字小更严谨,数字大更多样)",min_value=0.1,max_value=1.0,value=0.3,step=0.1)
submit=st.button("生成文章")
if submit:
    with st.spinner(("AI正在思考,请骚等")):
        title,script=generate_script(subject,number,genres,creativity,api_key)
    st.success("文章已经生成")
    st.subheader("标题")
    st.write(title)
    st.subheader("正文")
    st.write(script)
