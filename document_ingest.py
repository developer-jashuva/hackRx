# test_loader.py
import sys
import site
print(site.getsitepackages())  # Debug: See where packages are installed
sys.path.append("/path/to/your/site-packages")  # Adjust this based on output

from langchain_community.document_loaders import TextLoader

loader = TextLoader("./medical_data.txt", encoding="utf-8")
docs = loader.load()

print(f"Loaded {len(docs)} docs")
