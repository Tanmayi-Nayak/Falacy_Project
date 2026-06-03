from src.ingestion.read_docs import load_document
from src.preprocessing.structure_data import create_records
from src.preprocessing.save_json import save_json

# Load document
file_name = input("Enter file path (.txt or .docx): ")
text = load_document(file_name)

# Split text into sentences
sentences = text.split('.')
sentences = [s.strip() for s in sentences if s.strip()]

# Create and save records
records = create_records(sentences)
save_json(records)

print("Records saved successfully to data/processed/output.json")