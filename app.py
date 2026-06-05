import streamlit as st

st.title("Document Converter!!")

uploaded_file = st.file_uploader("Upload a document")

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image")
    st.success("Image Uploaded Successfully!")
