from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_texts(texts):
    return model.encode(texts, convert_to_tensor=True)

def rank_sections(persona, job, sections):
    persona_job_text = f"{persona}. {job}"
    query_vec = embed_texts([persona_job_text])[0]

    section_texts = [s['text'] for s in sections]
    doc_vecs = embed_texts(section_texts)

    similarities = cosine_similarity([query_vec], doc_vecs)[0]
    for i, sim in enumerate(similarities):
        sections[i]["score"] = float(sim)

    ranked = sorted(sections, key=lambda x: x["score"], reverse=True)
    return ranked[:10]
# model = SentenceTransformer('distiluse-base-multilingual-cased-v2')
model = SentenceTransformer('/app/pretrained_models/distiluse-base-multilingual-cased-v2')


