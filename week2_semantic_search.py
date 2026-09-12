from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

documents = [
    "Kazakh is an agglutinative Turkic language spoken mainly in Kazakhstan.",
    "The Basque language is a linguistic isolate spoken in northern Spain.",
    "Python is a popular programming language for data science and AI.",
    "RAG combines retrieval with a language model to reduce hallucinations.",
    "Attention lets a model look at all input tokens at once, not just a summary.",
]

doc_embeddings = model.encode(documents)

dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_embeddings))

query = "How does attention work in transformers?"
query_embedding = model.encode([query])

k = 2  # top 2 results
distances, indices = index.search(np.array(query_embedding), k)

with open("results_week2_semantic_search.txt", "w") as f:
    f.write(f"Query: {query}\n\n")
    for rank, idx in enumerate(indices[0]):
        line = f"Rank {rank+1}: \"{documents[idx]}\" (distance: {distances[0][rank]:.3f})\n"
        print(line)
        f.write(line)
