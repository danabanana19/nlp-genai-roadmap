from rdflib import Graph, Namespace, Literal, RDF

g = Graph()
n = Namespace("http://example.org/")

# Add triples: subject, predicate, object
g.add((n.Dana, n.studiesAt, n.UPVEHU))
g.add((n.Dana, n.speaks, n.Kazakh))
g.add((n.Dana, n.speaks, n.Russian))
g.add((n.Dana, n.speaks, n.Spanish))
g.add((n.Dana, n.worksOn, n.Thesis))
g.add((n.Thesis, n.studies, n.LLMs))
g.add((n.Thesis, n.coversLanguage, n.Kazakh))
g.add((n.Thesis, n.coversLanguage, n.Basque))

# Query: find everything Dana is connected to
query = """
SELECT ?predicate ?object
WHERE {
    <http://example.org/Dana> ?predicate ?object .
}
"""

with open("results_week3_kg.txt", "w") as f:
    for row in g.query(query):
        line = f"Dana --{row.predicate.split('/')[-1]}--> {row.object.split('/')[-1]}\n"
        print(line)
        f.write(line)
