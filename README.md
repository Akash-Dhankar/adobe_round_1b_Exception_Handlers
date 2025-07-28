# adobe_round_1b

This project is designed to rank sections of a document based on their semantic relevance to a given query using sentence embeddings. It uses the `sentence-transformers` library and a multilingual pre-trained model for semantic similarity, all containerized via Docker for easy and portable execution.

---

## 🚀 Features

- Embeds and ranks sections using `distiluse-base-multilingual-cased-v2` model
- Multilingual support for over 50 languages
- Fully Dockerized: no manual Python setup needed
- Efficient cosine similarity-based ranking logic

## 🧠 Approach & Methodology

### 1. Pretrained Model

We use `distiluse-base-multilingual-cased-v2`, a fast, lightweight transformer trained for semantic textual similarity. It allows us to embed and compare sentences in multiple languages.

To save time during container runs, we **pre-download and save** the model locally using:

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("distiluse-base-multilingual-cased-v2")
model.save("pretrained_models/distiluse-base-multilingual-cased-v2")


In embedder.py, we:
Load the sentence transformer model
Embed a query and list of document sections
Compute cosine similarity
Rank all sections by similarity score
This forms the core logic to extract the most relevant parts of a document.

A lightweight Docker image is built using python:3.9-slim, installing all dependencies and including the pre-saved model to ensure fast startup.
This makes the system portable and reproducible on any machine with Docker.

Docker Desktop installed and running
WSL2 integration enabled for Ubuntu (if using Windows)

1) CLONE THE REPO 
   git clone https://github.com/your-username/adobe-app.git
   cd adobe-app

2) docker build -t adobe-app .
3) docker run --rm -it -p 8000:8000 adobe-app



