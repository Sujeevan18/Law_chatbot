import os
import glob
from pypdf import PdfReader
from app.utils.text_cleaner import clean_text


def read_pdf(path: str) -> str:
    reader = PdfReader(path)
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n".join(pages)


def load_documents(data_dir: str):
    docs = []

    for path in glob.glob(os.path.join(data_dir, "**/*"), recursive=True):
        if os.path.isdir(path):
            continue

        ext = os.path.splitext(path)[1].lower()
        text = ""

        try:
            if ext == ".pdf":
                text = read_pdf(path)
            elif ext in [".txt", ".md"]:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read()
            else:
                continue

            text = clean_text(text)
            if text:
                docs.append({
                    "source": os.path.basename(path),
                    "path": path,
                    "text": text
                })
        except Exception as e:
            print(f"Skipping {path}: {e}")

    return docs


def chunk_text(text: str, chunk_size: int = 800, overlap: int = 150):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += max(1, chunk_size - overlap)

    return chunks