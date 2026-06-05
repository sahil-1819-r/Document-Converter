import streamlit as st
import img2pdf
from pdf2image import convert_from_bytes
from io import BytesIO

st.title("Document Converter")

# JPG/PNG TO PDF

st.header("Image to PDF Converter")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"],
    key="image_uploader"
)

if uploaded_file is not None:

    st.image(uploaded_file, caption="Uploaded Image")

    if st.button("Convert to PDF"):

        pdf_bytes = img2pdf.convert(uploaded_file.getvalue())

        st.download_button(
            label="Download PDF",
            data=pdf_bytes,
            file_name="converted.pdf",
            mime="application/pdf"
        )

        st.success("PDF Created Successfully!")


# PDF TO JPG


st.header("PDF to JPG Converter")

pdf_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"],
    key="pdf_uploader"
)

if pdf_file is not None:

    pages = convert_from_bytes(pdf_file.read())

    first_page = pages[0]

    st.image(first_page, caption="Preview")

    img_buffer = BytesIO()

    first_page.save(
        img_buffer,
        format="JPEG"
    )

    st.download_button(
        label="Download JPG",
        data=img_buffer.getvalue(),
        file_name="page1.jpg",
        mime="image/jpeg"
    )

    st.success("JPG Created Successfully!")