from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

pairs = [
    ("I love this course", "This class is amazing"),        # paraphrase
    ("I love this course", "I hate cold weather"),           # unrelated
    ("Мен бұл курсты жақсы көремін", "I love this course"),  # Kazakh-English paraphrase
]

with open("results_week2_embeddings.txt", "w") as f:
    for a, b in pairs:
        emb_a = model.encode(a, convert_to_tensor=True)
        emb_b = model.encode(b, convert_to_tensor=True)
        score = util.cos_sim(emb_a, emb_b).item()
        line = f"\"{a}\" <-> \"{b}\"\n  similarity: {score:.3f}\n"
        print(line)
        f.write(line)
