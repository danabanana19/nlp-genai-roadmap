from transformers import pipeline

mask_filler = pipeline("fill-mask", model="bert-base-multilingual-cased")

sentences = {
    "English": "I love learning [MASK].",
    "Kazakh": "Мен [MASK] оқуды жақсы көремін.",
}

with open("results_week1_fillmask.txt", "w") as f:
    for lang, text in sentences.items():
        results = mask_filler(text)
        line = f"\n{lang}: \"{text}\"\n"
        for r in results[:3]:
            line += f"  guess: {r['token_str']} (score: {r['score']:.3f})\n"
        print(line)
        f.write(line)
