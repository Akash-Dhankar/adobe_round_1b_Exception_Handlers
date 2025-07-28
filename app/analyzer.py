from keybert import KeyBERT

kw_model = KeyBERT('all-MiniLM-L6-v2')

def extract_keywords(text, n=5):
    keywords = kw_model.extract_keywords(text, top_n=n, stop_words='english')
    return [kw[0] for kw in keywords]

def refine_subsections(top_sections):
    refined = []
    for rank, sec in enumerate(top_sections, start=1):
        keywords = extract_keywords(sec["text"])
        refined.append({
            "document": sec["document"],
            "page": sec["page"],
            "refined_text": " ".join(keywords),
            "importance_rank": rank
        })
    return refined
