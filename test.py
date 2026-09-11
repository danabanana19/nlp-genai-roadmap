from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier("Мен бұл курсты жақсы көремін")
print(result)
