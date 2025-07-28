import os
import json
from extractor import extract_sections
from embedder import rank_sections
from analyzer import refine_subsections
from utils import load_text, current_timestamp

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"

def main():
    pdf_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".pdf")]
    persona = load_text(os.path.join(INPUT_DIR, "persona.txt"))
    job = load_text(os.path.join(INPUT_DIR, "job.txt"))

    all_sections = []
    for file in pdf_files:
        path = os.path.join(INPUT_DIR, file)
        sections = extract_sections(path)
        all_sections.extend(sections)

    ranked = rank_sections(persona, job, all_sections)
    refined = refine_subsections(ranked)

    output = {
        "metadata": {
            "documents": pdf_files,
            "persona": persona,
            "job_to_be_done": job,
            "timestamp": current_timestamp()
        },
        "extracted_sections": [
            {
                "document": s["document"],
                "page": s["page"],
                "section_title": s["text"][:60] + "...",
                "importance_rank": i + 1
            }
            for i, s in enumerate(ranked)
        ],
        "subsection_analysis": refined
    }

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "output.json"), "w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    main()
