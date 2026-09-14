# NLP / GenAI Learning Roadmap

I'm Dana Tussupbekova, an MSc student in Language Analysis and Processing at the University of the Basque Country (UPV/EHU), based in Donostia, Spain. 
I speak Kazakh, Russian, Spanish, and English, and my focus is multilingual and low-resource-language NLP.

This repo is my hands-on learning log as I build toward LLM/GenAI engineering roles — closing the gap between academic NLP and applied skills like RAG, semantic search, knowledge graphs, and fine-tuning. 
Every script here is something I built and ran myself, with results and notes documenting what I found, including bugs I hit and fixed along the way.

## Structure

- `week1_sentiment.py` — sentiment analysis, comparing model confidence across English and Kazakh
- `week1_fillmask.py` — masked-word prediction, same cross-language comparison
- `week2_tokenization.py` — comparing how a multilingual tokenizer splits English, Spanish, and Kazakh text
- `week2_embeddings.py` — cross-lingual sentence similarity using multilingual embeddings
- `week2_semantic_search.py` — a small semantic search engine built with FAISS
- `week3_hybrid_search.py` — hybrid retrieval combining BM25 (keyword) and embedding (meaning) search

Each script has a matching `results_*.txt` file with real output, and `notes/` contains my write-ups explaining what each experiment showed and why.

## A few findings so far

- A multilingual tokenizer needs roughly 2x as many tokens to represent Kazakh text as equivalent English text, with common words frequently fragmented — a concrete sign of how underrepresented Kazakh is in typical training data.
- Sentiment and fill-mask models perform noticeably worse and less confidently on Kazakh than on English.
- Multilingual sentence embeddings, by contrast, handle Kazakh well — a Kazakh sentence and its English translation scored *higher* similarity than two English paraphrases, suggesting embedding-based models generalize cross-lingually better than token-classification models.


More to come as I work through RAG, GraphRAG, agents, and fine-tuning over the next few months.
