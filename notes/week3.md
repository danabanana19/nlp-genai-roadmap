
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

## Knowledge Graphs — core concepts

A knowledge graph stores facts as **triples**: subject -> predicate -> object
(e.g. "Dana -> worksOn -> Thesis"). Three parts, always in this order. The
predicate (the "arrow") defines how the subject and object relate.

Triples chain together into a graph because an object in one triple can be
the subject of another -- e.g. "Dana -> worksOn -> Thesis" and
"Thesis -> studies -> LLMs" share "Thesis," which links the two facts.
This chaining is what lets you ask multi-hop questions (e.g. "what does
Dana's work eventually connect to?") that no single triple answers alone.

## Namespace
`Namespace("http://example.org/")` is just a shortcut so `n.Dana` expands
automatically to a full, unique ID (`http://example.org/Dana`) without
typing the whole address every time. The URL isn't a real website -- it's
borrowed purely because URLs are guaranteed unique, the same way a company
might assign unique employee IDs. `example.org` specifically is reserved
for examples and will never be a live site.

## Querying with SPARQL
SPARQL is a separate mini-language (not Python) for asking questions of a
graph. Inside a query, you can't use the Python `n.Dana` shortcut -- you
have to write the full `<http://example.org/Dana>` address, since SPARQL
doesn't know about Python's Namespace object.

In a query, anything written as a plain fixed value (e.g.
`<http://example.org/Dana>`) is a filter -- it won't appear in the results.
Anything marked with `?` (e.g. `?predicate`, `?object`) is a variable --
something you don't know yet and want the query to find. Any of the three
triple positions (subject, predicate, object) can be fixed or left as a
variable, depending on the question being asked:
- Fix subject, ask for predicate/object -> "what is X connected to?"
- Fix predicate, ask for subject/object -> "who/what has relationship Y?"
- Fix object, ask for subject/predicate -> "what points TO Z?"

## Multi-hop queries
Rather than one complex chained query, this can be done as two simple
queries run back to back: query 1 finds what's connected to Dana (e.g.
Thesis), query 2 then asks what's connected to Thesis (e.g. LLMs).
Breaking a hard question into two simple ones is a valid, often clearer
approach.

## Extracting triples from real sentences
A full natural sentence (with adjectives, extra description) doesn't map
directly to one triple -- you extract the core fact. E.g. "Dana, a
talented multilingual student, speaks fluent Kazakh" reduces to
"Dana -> speaks -> Kazakh." Descriptive detail (like "fluent") can be:
- folded into the relationship name itself (speaksFluently)
- attached as a separate property triple (Kazakh -> proficiencyLevel -> "fluent")
- or dropped entirely, if not useful for the graph's purpose
This connects directly to entity/relation extraction (e.g. spaCy NER) --
turning free text into structured triples is a real, non-trivial NLP task.

## Quads
A quad is a triple plus a 4th element -- a graph/context tag, e.g.
(Dana, speaks, Kazakh, self-reported). Useful for tracking where a fact
came from when combining data from multiple sources. rdflib supports this
via `ConjunctiveGraph()`/`Dataset()`. Not needed for this small graph, but
relevant for real multi-source knowledge graphs.


