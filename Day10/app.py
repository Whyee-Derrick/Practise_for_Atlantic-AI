import streamlit as st 
from pypdf import PdfReader

st.title ("file Reader")

uploaded = st.file_uploader("upload a file ",type=["pdf","txt"])

if uploaded is not None:
    if uploaded.name.endswith("txt"):
        text = uploaded.read().decode("utf-8")
    else:
        reader = PdfReader(uploaded) 
        text =""
        for page in reader.pages:
            text+=page.extract_text()   
    
    st.subheader("File contents")
    st.text_area("Text",text,height=600)        
    