# SEO Keyword Extractor (ColdFusion + Python)

This project extracts SEO-friendly keywords from any webpage URL using **ColdFusion (CFML)** and **Python (spaCy)**.  
It dynamically fetches a webpage, processes the content using NLP, and returns a list of optimized keywords for use in meta tags, ideal for SEO automation.

---

## 🔧 Features

- Extracts meaningful keywords using spaCy's NLP engine  
- Filters out irrelevant UI and navigation text dynamically  
- Integrates ColdFusion `<cfhttp>` and `<cfexecute>` to run Python  
- Automatically deletes temporary HTML file after processing  
- Optimized for generating dynamic `<meta name="keywords">` tags  

---

## 🚀 Getting Started

### Install Python Dependencies

> Make sure you're using Python **3.8 to 3.11** (avoid 3.13+ for better library compatibility)

```bash
pip install beautifulsoup4 spacy
python -m spacy download en_core_web_sm 
```

---

## 🐍 Python Script Overview

- Reads HTML file passed as an argument
- Uses BeautifulSoup and spaCy to clean and process text
- Dynamically filters out irrelevant content (non-ASCII, common UI terms, etc.)
- Outputs top 25 SEO-relevant keywords
- Deletes the temporary file automatically after processing

---

## Developer

Gaurav Sharma <br>
gaurav110601@gmail.com <br>
> [LinkedIn](https://www.linkedin.com/in/gaurav110601/)