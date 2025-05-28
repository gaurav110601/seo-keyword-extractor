import sys
import io
import os
import re
from bs4 import BeautifulSoup
from collections import Counter
import spacy

# Ensure UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except Exception as e:
    print(f"Error loading spaCy model: {e}")
    sys.exit(1)

def clean_text(text):
    """Cleans text by removing extra whitespace and special characters."""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s\-]', '', text)
    return text.strip()

def extract_keywords(html_content, top_n=25):
    """Extracts top N keywords (NOUNS, PROPNs) from the cleaned HTML text."""
    soup = BeautifulSoup(html_content, "html.parser")

    # Remove non-content tags
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "svg"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)
    text = clean_text(text)
    doc = nlp(text)

    keywords = [
        token.lemma_.lower()
        for token in doc
        if token.is_alpha and not token.is_stop and len(token.text) > 3 and token.pos_ in {"NOUN", "PROPN"} and token.lemma_.isascii()
    ]

    counts = Counter(keywords)
    return [kw for kw, _ in counts.most_common(top_n)]

def main(html_file_path):
    """Main logic: reads file, extracts keywords, prints, and deletes temp file."""
    if not os.path.isfile(html_file_path):
        print(f"Error: File not found - {html_file_path}")
        return

    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        keywords = extract_keywords(html_content)
        print(",".join(keywords))

    except Exception as e:
        print(f"Error processing file: {e}")
    finally:
        try:
            os.remove(html_file_path)
        except Exception as e:
            print(f"Warning: Could not delete temp file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_keywords_spacy.py <html_file_path>")
        sys.exit(1)

    main(sys.argv[1])
