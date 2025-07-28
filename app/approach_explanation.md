### Approach Explanation

In this solution, we simulate a document intelligence system that surfaces the most relevant sections from a set of PDFs based on a given persona and job-to-be-done.

**Step 1: Text Extraction**
We parse each PDF using PyMuPDF, extracting paragraphs and their page numbers.

**Step 2: Persona Understanding**
We read the persona and job descriptions from plain text files, treating them as a "query".

**Step 3: Embedding & Similarity**
Using Sentence Transformers (MiniLM), we compute semantic embeddings of both query and section texts, then use cosine similarity to rank them.

**Step 4: Subsection Analysis**
The top-10 ranked sections are analyzed using KeyBERT to extract refined insights. Each section is assigned an importance rank.

**Step 5: Output Generation**
Results are saved in structured JSON format with metadata, top ranked sections, and refined subsection highlights.

This solution is modular, scalable, and CPU-friendly. It runs offline and adheres to model size limits.
