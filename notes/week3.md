
## Hybrid retrieval (BM25 + embeddings)
Combined keyword-based BM25 with embedding-based semantic search for query
"What is RAG?" against the same 5-document set.

Bug found: naive tokenization (.split() on raw text) left punctuation stuck
to words (e.g. "rag?" instead of "rag"), causing BM25 to completely miss
the correct document (score 0.000) despite an exact keyword match existing.
Fixed by stripping punctuation before tokenizing.

After the fix: the RAG document scored a perfect 1.000 on both BM25 and
embeddings, correctly ranking first. This is a real example of why
production retrieval systems need careful text preprocessing -- a small
tokenization bug can silently break exact-match retrieval even when the
answer is obviously present in the data.
