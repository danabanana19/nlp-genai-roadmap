from sentence_transformers import SentenceTransformer, util
from rank_bm25 import BM25Okapi
import numpy as np
import re

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

documents = [
    "Kazakh is an agglutinative Turkic language spoken mainly in Kazakhstan.",
    "The Basque language is a linguistic isolate spoken in northern Spain.",
    "Python is a popular programming language for data science and AI.",
    "RAG combines retrieval with a language model to reduce hallucinations.",
    "Attention lets a model look at all input tokens at once, not just a summary.",
]

def clean_tokenize(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text.split()

query = "What is RAG?"

# --- BM25 setup (keyword-based) ---
tokenized_docs = [clean_tokenize(doc) for doc in documents]
bm25 = BM25Okapi(tokenized_docs)
bm25_scores = bm25.get_scores(clean_tokenize(query))

# --- Embedding setup (meaning-based) ---
doc_embeddings = model.encode(documents, convert_to_tensor=True)
query_embedding = model.encode(query, convert_to_tensor=True)
embed_scores = util.cos_sim(query_embedding, doc_embeddings)[0].cpu().numpy()

# Normalize both score sets to 0-1 so they're comparable, then combine
def normalize(scores):
    return (scores - scores.min()) / (scores.max() - scores.min() + 1e-9)

bm25_norm = normalize(bm25_scores)
embed_norm = normalize(embed_scores)

hybrid_scores = 0.5 * bm25_norm + 0.5 * embed_norm

ranked = np.argsort(hybrid_scores)[::-1]

with open("results_week2_hybrid.txt", "w") as f:
    f.write(f"Query: {query}\n\n")
    for rank, idx in enumerate(ranked):
        line = (f"Rank {rank+1}: \"{documents[idx]}\"\n"
                f"  bm25={bm25_norm[idx]:.3f}  embed={embed_norm[idx]:.3f}  "
                f"hybrid={hybrid_scores[idx]:.3f}\n")
        print(line)
        f.write(line)
