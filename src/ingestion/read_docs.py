from pathlib import Path
from docx import Document

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_word_file(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def load_document(file_path):
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.suffix.lower() == '.txt':
        return read_text_file(file_path)

    elif file_path.suffix.lower() == '.docx':
        return read_word_file(file_path)

    else:
        raise ValueError("Unsupported file format. Use .txt or .docx")

# User input
file_name = input("Enter file path (.txt or .docx): ")

try:
    text = load_document(file_name)

    print("\nDocument loaded successfully!")
    print(f"Total characters: {len(text)}")

    # NLP processing starts here
    # Example:
    # tokens = tokenizer(text)
    # sentiment = analyze_sentiment(text)

    print("\nPreview:")
    print(text[:500])

except Exception as e:
    print(f"Error: {e}")
    