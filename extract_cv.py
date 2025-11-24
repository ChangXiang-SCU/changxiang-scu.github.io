import pypdf
import json
import re

def extract_cv_data(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    text_content = ""
    links = []

    for page in reader.pages:
        text_content += page.extract_text() + "\n"
        if "/Annots" in page:
            for annot in page["/Annots"]:
                obj = annot.get_object()
                if "/A" in obj and "/URI" in obj["/A"]:
                    uri = obj["/A"]["/URI"]
                    links.append(uri)

    # Basic parsing (this is heuristic and might need adjustment)
    data = {
        "raw_text": text_content,
        "links": links
    }
    
    with open("cv_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("Data written to cv_data.json")

if __name__ == "__main__":
    extract_cv_data("Xiang Chang-CV-full 2025.pdf")
