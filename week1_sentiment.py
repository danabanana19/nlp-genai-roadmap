from transformers import pipeline

classifier = pipeline("sentiment-analysis")

sentences = {
    "English": "I love learning NLP",
    "Kazakh": "Мен бұл курсты жақсы көремін",
}

with open("results_week1_sentiment.txt", "w") as f:
    for lang, text in sentences.items():
        result = classifier(text)
        line = f"{lang}: \"{text}\" -> {result}"
        print(line)
        f.write(line + "\n")
