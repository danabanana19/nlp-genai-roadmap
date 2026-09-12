Tokenization comparison (bert-base-multilingual-cased):
- English: 7 words -> 7 tokens (1.0x)
- Spanish: 8 words -> 10 tokens (1.25x)
- Kazakh: 8 words -> 16 tokens (2.0x)
Kazakh required double the tokens of English for a similar-length sentence,
with even short common words fragmented into 3-4 pieces. This reflects
Kazakh's low representation in multilingual training data.

English: "I love learning about language models."
  tokens (7): ['I', 'love', 'learning', 'about', 'language', 'models', '.']

Kazakh: "Мен тіл модельдері туралы білім алуды жақсы көремін."
  tokens (16): ['М', '##ен', 'ті', '##л', 'модель', '##дері', 'туралы', 'білім', 'алу', '##ды', 'жақсы', 'к', '##өр', '##ем', '##ін', '.']

Spanish: "Me encanta aprender sobre modelos de lenguaje."
  tokens (10): ['Me', 'en', '##cant', '##a', 'aprender', 'sobre', 'modelos', 'de', 'lenguaje', '.']


## Embeddings: cross-lingual similarity
"I love this course" <-> "This class is amazing" (paraphrase): 0.735
"I love this course" <-> "I hate cold weather" (unrelated): 0.010
Kazakh "Мен бұл курсты жақсы көремін" <-> English "I love this course": 0.766

Notable: the Kazakh-English pair scored HIGHER than the English paraphrase
pair, despite zero surface word overlap and different scripts. Unlike the
sentiment/fill-mask models tested in week 1, this multilingual embedding
model handles Kazakh well -- suggesting model architecture/training
objective matters more than just "is Kazakh represented," since embedding
models seem to generalize cross-lingually better than token-classification
models tested earlier.
