import streamlit as st

st.title("Hacking for Myanmar - AI OCR")
st.subheader("Optical Character Recongnition with Voice Input")
st.text("select source language from side bar")

image = st.file_uploader("Upload Image", ["JPG", "PNG"])

if st.button("Convert"):
    pass

st.sidebar.title("Langugae Selection Menu")

st.sidebar.subheader("Select....")

from_language = st.sidebar.selectbox("Form Language", ["English", "French"])
st.write("")

st.sidebar.subheader("Select....")

to_language = st.sidebar.selectbox("To Language", ["English", "French"])

st.sidebar.write()
st.sidebar.subheader("Enter Text")
st.sidebar.text_area("Auto Detection Enabled")

if st.sidebar.button("Translate"):
    pass
