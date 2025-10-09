"""
Утилиты для извлечения текста из разных форматов файлов
"""

import asyncio
import fitz
from docx import Document

async def extract_txt(file_path: str) -> str:
    """Извлечение текста из TXT файла"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

async def extract_docx(file_path: str) -> str:
    """Извлечение текста из DOCX файла"""
    doc = Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)

async def extract_pdf(file_path: str) -> str:
    """Извлечение текста из PDF файла"""
    text = []
    with fitz.open(file_path) as doc:
        for page in doc:
            text.append(page.get_text())
    return '\n'.join(text)
