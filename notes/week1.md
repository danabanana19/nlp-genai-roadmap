
## Sentiment analysis: English vs Kazakh
English: "I love learning NLP" -> POSITIVE (99.96% confidence)
Kazakh: "Мен бұл курсты жақсы көремін" -> NEGATIVE (64.49% confidence, incorrect)

Same positive meaning in both languages, but the model got Kazakh wrong,
and with much lower confidence than English. This reflects how models
trained mostly on English data don't generalize well to lower-resource
languages like Kazakh.

## Fill-mask: English vs Kazakh
English: "I love learning [MASK]." -> top guess "learning" (10.3% confidence)
Kazakh: "Мен [MASK] оқуды жақсы көремін." -> top guess "мен" (11.3% confidence,
does not fit grammatically)

Note: English confidence was also low here (10.3%), much lower than the
sentiment task. This suggests fill-mask is a harder task in general, not
purely a Kazakh-specific weakness -- worth separating "task is hard" from
"language is underrepresented" when interpreting results.
