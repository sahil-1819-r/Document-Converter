import streamlit as st
import img2pdf
from pdf2image import convert_from_bytes
from io import BytesIO
import pytesseract
from PIL import Image


st.title("Document Converter")

# JPG/PNG TO PDF

st.header("Image to PDF Converter")

uploaded_file = st.file_uploader( "Upload Image",type=["jpg", "jpeg", "png"],key="image_uploader")

if uploaded_file is not None:

    st.image(uploaded_file, caption="Uploaded Image")

    if st.button("Convert to PDF"):

        pdf_bytes = img2pdf.convert(uploaded_file.getvalue())

        downloaded = st.download_button(
            label="Download PDF",
            data=pdf_bytes,
            file_name="converted.pdf",
            mime="application/pdf"
        )

        st.success("PDF Created Successfully!")


# PDF TO JPG


st.header("PDF to JPG Converter")

pdf_file = st.file_uploader("Upload PDF",type=["pdf"],key="pdf_uploader")

if pdf_file is not None:

    pages = convert_from_bytes(pdf_file.read())

    first_page = pages[0]

    st.image(first_page, caption="Preview")

    img_buffer = BytesIO()

    first_page.save(
        img_buffer,
        format="JPEG"
    )

    downloaded_pdf =st.download_button(
        label="Download JPG",
        data=img_buffer.getvalue(),
        file_name="page1.jpg",
        mime="image/jpeg"
    )
    st.success("JPG Created Successfully!")
    
    if downloaded_pdf:
            st.success("Downloaded Successfully!")
            

# OCR Text Extractor


st.header("Text Extractor")

ocr_file = st.file_uploader("Upload Image for OCR",type=["jpg", "jpeg", "png"],key="ocr_uploader")

if ocr_file is not None:

    image = Image.open(ocr_file)

    st.image(image, caption="Uploaded Image")

    if st.button("Extract Text"):

        extracted_text = pytesseract.image_to_string(image)

        st.success("Text Extracted Successfully! ✅")

        edited_text = st.text_area(
            "Extracted Text",
            value=extracted_text,
            height=300
        )

        st.download_button(
            "Download Text",
            data=edited_text,
            file_name="extracted_text.txt",
            mime="text/plain"
        )


# PDF OCR Text Extractor

st.header("PDF Text Extractor")

pdf_ocr_file = st.file_uploader("Upload PDF",type=["pdf"],key="pdf_ocr_uploader")

if pdf_ocr_file is not None:

    if st.button("Extract Text from PDF"):

        pages = convert_from_bytes(pdf_ocr_file.read())

        extracted_text = ""

        for page in pages:
            extracted_text += pytesseract.image_to_string(page)
            extracted_text += "\n\n"

        st.success("Text Extracted Successfully! ✅")

        edited_pdf_text = st.text_area(
            "Extracted PDF Text",
            value=extracted_text,
            height=300
        )

        st.download_button(
            "Download PDF Text",
            data=edited_pdf_text,
            file_name="pdf_extracted_text.txt",
            mime="text/plain"
        )  