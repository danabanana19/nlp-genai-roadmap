from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")

sentences = {
    "English": "I love learning about language models.",
    "Kazakh": "Мен тіл модельдері туралы білім алуды жақсы көремін.",
    "Spanish": "Me encanta aprender sobre modelos de lenguaje.",
}

with open("results.txt", "w") as f:
    for lang, text in sentences.items():
        tokens = tokenizer.tokenize(text)
        line = f"\n{lang}: \"{text}\"\n  tokens ({len(tokens)}): {tokens}\n"
        print(line)
        f.write(line)

