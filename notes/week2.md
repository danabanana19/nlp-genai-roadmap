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
