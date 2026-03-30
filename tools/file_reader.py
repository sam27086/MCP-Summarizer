from pypdf import PdfReader
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os

# ---------------- Text Reader ----------------
def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# ---------------- Image Reader ----------------
def read_image_file(file_path):
    image = Image.open(file_path)
    return pytesseract.image_to_string(image)

# ---------------- PDF Reader ----------------
def read_pdf_file(file_path, use_ocr=False):
    reader = PdfReader(file_path)
    text = ""

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text()
        # If empty and OCR is enabled
        if (not page_text) and use_ocr:
            images = convert_from_path(file_path, first_page=page_number, last_page=page_number)
            ocr_text = "".join(pytesseract.image_to_string(img) for img in images)
            page_text = ocr_text
        text += (page_text or "") + " "
    return text.strip()

# ---------------- Unified Reader ----------------
def read_file(file_path, tool_name):
    tool_name = tool_name.lower()
    if tool_name == "pdf_reader":
        return read_pdf_file(file_path, use_ocr=False)
    elif tool_name == "image_pdf_reader":
        return read_pdf_file(file_path, use_ocr=True)
    elif tool_name == "image_reader":
        return read_image_file(file_path)
    elif tool_name == "text_reader":
        return read_text_file(file_path)
    else:
        raise ValueError(f"Unknown tool: {tool_name}")