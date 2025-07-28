import fitz  # PyMuPDF

def extract_sections(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []

    for i, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            text = ""
            for line in block["lines"]:
                for span in line["spans"]:
                    text += span["text"].strip() + " "
            text = text.strip()
            if text:
                sections.append({
                    "document": pdf_path.split("/")[-1],
                    "page": i,
                    "text": text
                })

    return sections
