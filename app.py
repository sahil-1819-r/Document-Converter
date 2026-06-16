import os
import subprocess
import tempfile
from io import BytesIO

import img2pdf
import pytesseract
import streamlit as st
from pdf2docx import Converter
from pdf2image import convert_from_bytes
from PIL import Image


APP_VERSION = "v1.0.0"

TOOLS = {
    "Image to PDF": {
        "icon": "🖼️",
        "description": "Convert JPG, JPEG, and PNG images into polished PDF files.",
        "button": "Convert Now",
        "color": "pink",
    },
    "PDF to JPG": {
        "icon": "🧾",
        "description": "Turn the first page of a PDF into a high-quality JPG image.",
        "button": "Convert Now",
        "color": "orange",
    },
    "DOCX to PDF": {
        "icon": "📗",
        "description": "Convert Word DOCX documents into shareable PDF files.",
        "button": "Convert Now",
        "color": "green",
    },
    "PDF to DOCX": {
        "icon": "📘",
        "description": "Convert PDF documents into editable Word DOCX files.",
        "button": "Convert Now",
        "color": "blue",
    },
    "Image OCR": {
        "icon": "🔎",
        "description": "Extract text from JPG, JPEG, and PNG image files.",
        "button": "Extract Text",
        "color": "teal",
    },
    "PDF OCR": {
        "icon": "📝",
        "description": "Extract readable text from PDF pages using OCR.",
        "button": "Extract Text",
        "color": "purple",
    },
}


def load_css() -> None:
    with open("assets/style.css", "r", encoding="utf-8") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)


def apply_theme(theme: str) -> None:
    if theme == "Light":
        theme_css = """
        <style>
        :root {
            --app-bg: #f6f8fc;
            --panel-bg: rgba(255, 255, 255, 0.86);
            --panel-solid: #ffffff;
            --text-primary: #111d35;
            --text-secondary: #52607a;
            --text-muted: #77829a;
            --border-soft: rgba(37, 51, 80, 0.12);
            --shadow-soft: 0 24px 70px rgba(32, 46, 84, 0.12);
            --shadow-card: 0 14px 38px rgba(32, 46, 84, 0.10);
            --input-bg: #ffffff;
            --code-bg: #111827;
            --code-text: #e8eefc;
            --text-on-accent: #ffffff;
            --hero-bg: linear-gradient(120deg, rgba(224, 247, 255, 0.92), rgba(255, 255, 255, 0.82) 42%, rgba(255, 226, 248, 0.86));
            --hero-doc-bg: rgba(255, 255, 255, 0.82);
        }
        </style>
        """
    elif theme == "Dark":
        theme_css = """
        <style>
        :root {
            --app-bg: #09111f;
            --panel-bg: rgba(16, 25, 42, 0.84);
            --panel-solid: #111a2b;
            --text-primary: #edf4ff;
            --text-secondary: #b8c5dd;
            --text-muted: #8794ad;
            --border-soft: rgba(213, 224, 255, 0.14);
            --shadow-soft: 0 26px 72px rgba(0, 0, 0, 0.34);
            --shadow-card: 0 16px 44px rgba(0, 0, 0, 0.28);
            --input-bg: #121c2f;
            --code-bg: #050914;
            --code-text: #ecf4ff;
            --text-on-accent: #ffffff;
            --hero-bg: linear-gradient(120deg, rgba(20, 42, 69, 0.96), rgba(17, 26, 43, 0.90) 44%, rgba(49, 30, 73, 0.84));
            --hero-doc-bg: rgba(20, 28, 46, 0.88);
        }
        </style>
        """
    else:
        theme_css = ""

    if theme_css:
        st.markdown(theme_css, unsafe_allow_html=True)


def ensure_theme_state() -> None:
    if "theme_mode" not in st.session_state:
        st.session_state.theme_mode = "Light"


def toggle_theme() -> None:
    st.session_state.theme_mode = "Dark" if st.session_state.theme_mode == "Light" else "Light"


def set_selected_tool(tool_name: str) -> None:
    st.session_state.selected_tool = tool_name


def render_sidebar() -> str:
    if "selected_tool" not in st.session_state:
        st.session_state.selected_tool = "Dashboard"

    with st.sidebar:
        st.markdown(
            """
            <div class="brand-block">
                <div class="brand-logo">▰</div>
                <div>
                    <div class="brand-title">DocuConvert</div>
                    <div class="brand-subtitle">All-in-One Converter & OCR</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

        if st.button("⌂  Dashboard", key="nav_dashboard", use_container_width=True):
            set_selected_tool("Dashboard")

        st.markdown('<div class="nav-section">Converters</div>', unsafe_allow_html=True)
        for tool in ["Image to PDF", "PDF to JPG", "DOCX to PDF", "PDF to DOCX"]:
            if st.button(f"{TOOLS[tool]['icon']}  {tool}", key=f"nav_{tool}", use_container_width=True):
                set_selected_tool(tool)

        st.markdown('<div class="nav-section">OCR Tools</div>', unsafe_allow_html=True)
        for tool in ["Image OCR", "PDF OCR"]:
            if st.button(f"{TOOLS[tool]['icon']}  {tool}", key=f"nav_{tool}", use_container_width=True):
                set_selected_tool(tool)

        st.markdown('<div class="nav-section">Others</div>', unsafe_allow_html=True)
        for page in ["About", "How to Use"]:
            if st.button(f"ⓘ  {page}", key=f"nav_{page}", use_container_width=True):
                set_selected_tool(page)

        st.markdown(
            """
            <div class="upgrade-card">
                <div class="upgrade-icon">★</div>
                <strong>Upgrade Coming Soon</strong>
                <span>More powerful batch tools and premium workflows are on the way.</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    return st.session_state.selected_tool


def render_top_header() -> None:
    left, right = st.columns([1, 1])
    with left:
        st.markdown(
            """
            <div class="top-kicker">Dashboard</div>
            <h1 class="page-title">Document Converter & OCR Tool</h1>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.markdown('<div class="theme-toggle-anchor"></div>', unsafe_allow_html=True)
        theme_icon = "🌙" if st.session_state.theme_mode == "Dark" else "☀️"
        if st.button(theme_icon, key="theme_toggle", help="Toggle theme"):
            toggle_theme()
            st.rerun()


def render_hero() -> None:
    st.markdown(
        """
        <section class="hero-banner">
            <div class="hero-copy">
                <h2>Document Converter & OCR Tool 🚀</h2>
                <p>Convert, Extract, and Transform your documents with ease. Fast, Secure, and Completely Free.</p>
                <div class="hero-badges">
                    <span>🎁 100% Free</span>
                    <span>🔒 Secure</span>
                    <span>⚡ Fast</span>
                    <span>🙂 Easy to Use</span>
                </div>
            </div>
            <div class="hero-illustration" aria-label="Document conversion illustration">
                <div class="doc-card doc-pdf">PDF</div>
                <div class="doc-card doc-docx">DOCX</div>
                <div class="doc-card doc-img">IMG</div>
                <div class="arrow arrow-one">↻</div>
                <div class="arrow arrow-two">➜</div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_dashboard_cards() -> None:
    st.markdown('<h3 class="section-title">⭐ Choose a Tool</h3>', unsafe_allow_html=True)

    rows = [
        ["Image to PDF", "PDF to JPG", "DOCX to PDF"],
        ["PDF to DOCX", "Image OCR", "PDF OCR"],
    ]

    for row in rows:
        columns = st.columns(3)
        for column, tool in zip(columns, row):
            data = TOOLS[tool]
            with column:
                st.markdown(
                    f"""
                    <div class="feature-card feature-{data['color']}">
                        <div class="feature-icon">{data['icon']}</div>
                        <div class="feature-copy">
                            <h4>{tool}</h4>
                            <p class="feature-description">{data['description']}</p>
                        </div>
                    </div>
                    <div class="dashboard-card-action"></div>
                    """,
                    unsafe_allow_html=True,
                )
                if st.button(f"{data['button']}  →", key=f"card_{tool}", use_container_width=True):
                    set_selected_tool(tool)
                    st.rerun()


def render_benefits() -> None:
    benefits = [
        ("🛡️", "Your Privacy Matters", "Your files are processed locally in this app session."),
        ("⚡", "Lightning Fast", "Get conversions and extractions done in seconds."),
        ("✓", "High Quality", "Preserve document quality across every workflow."),
        ("▣", "Works Everywhere", "Use the tools from any device with a browser."),
    ]

    st.markdown('<div class="benefits-grid">', unsafe_allow_html=True)
    columns = st.columns(4)
    for column, (icon, title, text) in zip(columns, benefits):
        with column:
            st.markdown(
                f"""
                <div class="benefit-card">
                    <div class="benefit-icon">{icon}</div>
                    <div>
                        <h4>{title}</h4>
                        <p>{text}</p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    st.markdown("</div>", unsafe_allow_html=True)


def render_file_info(uploaded_file) -> None:
    if uploaded_file is None:
        return

    size_kb = len(uploaded_file.getvalue()) / 1024
    file_type = uploaded_file.type or "Unknown"
    st.markdown(
        f"""
        <div class="file-info-card">
            <div class="file-info-icon">📄</div>
            <div>
                <strong>{uploaded_file.name}</strong>
                <span>{size_kb:,.1f} KB • {file_type}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def tool_header(title: str, description: str) -> None:
    st.markdown(
        f"""
        <div class="tool-header">
            <div class="tool-icon" aria-hidden="true">{TOOLS[title]['icon']}</div>
            <div class="tool-copy">
                <h2>{title}</h2>
                <p>{description}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def back_button() -> None:
    st.markdown('<div class="back-button-anchor"></div>', unsafe_allow_html=True)
    if st.button("← Back to Dashboard", key=f"back_to_dashboard_{st.session_state.selected_tool}"):
        set_selected_tool("Dashboard")
        st.rerun()


def render_image_to_pdf() -> None:
    tool_header("Image to PDF", "Upload an image and convert it into a PDF document.")
    back_button()
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"], key="image_uploader")
    render_file_info(uploaded_file)

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

        if st.button("Convert to PDF", type="primary"):
            pdf_bytes = img2pdf.convert(uploaded_file.getvalue())
            st.download_button(
                label="Download PDF",
                data=pdf_bytes,
                file_name="converted.pdf",
                mime="application/pdf",
            )
            st.success("PDF Created Successfully!")


def render_pdf_to_jpg() -> None:
    tool_header("PDF to JPG", "Upload a PDF and download the first page as a JPG image.")
    back_button()
    pdf_file = st.file_uploader("Upload PDF", type=["pdf"], key="pdf_uploader")
    render_file_info(pdf_file)

    if pdf_file is not None:
        pages = convert_from_bytes(pdf_file.read())
        first_page = pages[0]
        st.image(first_page, caption="Preview", use_container_width=True)

        img_buffer = BytesIO()
        first_page.save(img_buffer, format="JPEG")

        downloaded_pdf = st.download_button(
            label="Download JPG",
            data=img_buffer.getvalue(),
            file_name="page1.jpg",
            mime="image/jpeg",
        )
        st.success("JPG Created Successfully!")

        if downloaded_pdf:
            st.success("Downloaded Successfully!")


def render_image_ocr() -> None:
    tool_header("Image OCR", "Upload an image and extract editable text with OCR.")
    back_button()
    ocr_file = st.file_uploader("Upload Image for OCR", type=["jpg", "jpeg", "png"], key="ocr_uploader")
    render_file_info(ocr_file)

    if ocr_file is not None:
        image = Image.open(ocr_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        if st.button("Extract Text", type="primary"):
            extracted_text = pytesseract.image_to_string(image)
            st.success("Text Extracted Successfully! ✅")

            st.markdown('<div class="ocr-output-label">Extracted Text</div>', unsafe_allow_html=True)
            edited_text = st.text_area("Extracted Text", value=extracted_text, height=300, label_visibility="collapsed")

            st.download_button(
                "Download Text",
                data=edited_text,
                file_name="extracted_text.txt",
                mime="text/plain",
            )


def render_pdf_ocr() -> None:
    tool_header("PDF OCR", "Upload a PDF and extract text from each page.")
    back_button()
    pdf_ocr_file = st.file_uploader("Upload PDF", type=["pdf"], key="pdf_ocr_uploader")
    render_file_info(pdf_ocr_file)

    if pdf_ocr_file is not None:
        if st.button("Extract Text from PDF", type="primary"):
            pages = convert_from_bytes(pdf_ocr_file.read())
            extracted_text = ""

            for page in pages:
                extracted_text += pytesseract.image_to_string(page)
                extracted_text += "\n\n"

            st.success("Text Extracted Successfully! ✅")

            st.markdown('<div class="ocr-output-label">Extracted PDF Text</div>', unsafe_allow_html=True)
            edited_pdf_text = st.text_area(
                "Extracted PDF Text",
                value=extracted_text,
                height=300,
                label_visibility="collapsed",
            )

            st.download_button(
                "Download PDF Text",
                data=edited_pdf_text,
                file_name="pdf_extracted_text.txt",
                mime="text/plain",
            )


def render_docx_to_pdf() -> None:
    tool_header("DOCX to PDF", "Upload a DOCX file and convert it into a PDF document.")
    back_button()
    docx_file = st.file_uploader("Upload DOCX", type=["docx"], key="docx_uploader")
    render_file_info(docx_file)

    if docx_file is not None:
        if st.button("Convert DOCX to PDF", type="primary"):
            with tempfile.TemporaryDirectory() as temp_dir:
                docx_path = os.path.join(temp_dir, "input.docx")

                with open(docx_path, "wb") as f:
                    f.write(docx_file.getbuffer())

                subprocess.run(
                    [
                        "libreoffice",
                        "--headless",
                        "--convert-to",
                        "pdf",
                        docx_path,
                        "--outdir",
                        temp_dir,
                    ],
                    check=True,
                )

                pdf_path = os.path.join(temp_dir, "input.pdf")

                with open(pdf_path, "rb") as pdf_file:
                    pdf_bytes = pdf_file.read()

                st.success("PDF Created Successfully! ✅")

                downloaded_docx_pdf = st.download_button(
                    "Download PDF",
                    data=pdf_bytes,
                    file_name="converted.pdf",
                    mime="application/pdf",
                )

                if downloaded_docx_pdf:
                    st.success("Downloaded Successfully! ✅")


def render_pdf_to_docx() -> None:
    tool_header("PDF to DOCX", "Upload a PDF file and convert it into an editable DOCX document.")
    back_button()
    pdf_docx_file = st.file_uploader("Upload PDF", type=["pdf"], key="pdf_docx_uploader")
    render_file_info(pdf_docx_file)

    if pdf_docx_file is not None:
        if st.button("Convert PDF to DOCX", type="primary"):
            with tempfile.TemporaryDirectory() as temp_dir:
                pdf_path = os.path.join(temp_dir, "input.pdf")

                with open(pdf_path, "wb") as f:
                    f.write(pdf_docx_file.getbuffer())

                docx_path = os.path.join(temp_dir, "output.docx")

                cv = Converter(pdf_path)
                cv.convert(docx_path)
                cv.close()

                with open(docx_path, "rb") as docx_file:
                    docx_bytes = docx_file.read()

                st.success("DOCX Created Successfully! ✅")

                downloaded_pdf_docx = st.download_button(
                    "Download DOCX",
                    data=docx_bytes,
                    file_name="converted.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                )

                if downloaded_pdf_docx:
                    st.success("Downloaded Successfully! ✅")


def render_about() -> None:
    st.markdown('<div class="info-panel">', unsafe_allow_html=True)
    st.subheader("About DocuConvert")
    back_button()
    st.write(
        "DocuConvert is a free document conversion and OCR workspace built with Streamlit. "
        "It converts common file formats and extracts text from images or PDFs in a clean dashboard interface."
    )
    with st.expander("Included tools", expanded=True):
        st.write("Image to PDF, PDF to JPG, DOCX to PDF, PDF to DOCX, Image OCR, and PDF OCR.")
    with st.expander("Privacy note"):
        st.write("Uploaded files are handled inside the running app session and are not stored by this interface.")
    st.markdown("</div>", unsafe_allow_html=True)


def render_how_to_use() -> None:
    st.subheader("How to Use")
    back_button()
    tabs = st.tabs(["Converters", "OCR Tools", "Downloads"])
    with tabs[0]:
        st.write("Choose a converter from the sidebar, upload the requested file type, then run the conversion.")
    with tabs[1]:
        st.write("Choose Image OCR or PDF OCR, upload your source file, and extract editable text.")
    with tabs[2]:
        st.write("After processing completes, use the download button to save the generated file or text output.")


def render_footer() -> None:
    st.markdown(
        f"""
        <footer class="app-footer">
            <span>Made with ❤️ by Sahil</span>
            <a href="https://github.com/" target="_blank" rel="noreferrer">GitHub</a>
            <span>Document Converter & OCR Tool</span>
            <span>{APP_VERSION}</span>
            <span>© 2026 All Rights Reserved</span>
        </footer>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    st.set_page_config(
        page_title="DocuConvert - Document Converter & OCR Tool",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    load_css()
    ensure_theme_state()
    apply_theme(st.session_state.theme_mode)
    selected_tool = render_sidebar()
    render_top_header()

    with st.container():
        if selected_tool == "Dashboard":
            render_hero()
            render_dashboard_cards()
            render_benefits()
        elif selected_tool == "Image to PDF":
            render_image_to_pdf()
        elif selected_tool == "PDF to JPG":
            render_pdf_to_jpg()
        elif selected_tool == "DOCX to PDF":
            render_docx_to_pdf()
        elif selected_tool == "PDF to DOCX":
            render_pdf_to_docx()
        elif selected_tool == "Image OCR":
            render_image_ocr()
        elif selected_tool == "PDF OCR":
            render_pdf_ocr()
        elif selected_tool == "About":
            render_about()
        elif selected_tool == "How to Use":
            render_how_to_use()

    render_footer()


if __name__ == "__main__":
    main()
