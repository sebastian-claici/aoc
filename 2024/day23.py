import sys
import networkx as nx

from aocd.models import Puzzle


puzzle = Puzzle(year=2024, day=23)
data = puzzle.input_data

G = nx.Graph()

for line in data.split("\n"):
    a, b = line.strip().split("-")
    G.add_edge(a, b)

three_cliques = 0
max_clique = 0
password = ""
for c in nx.enumerate_all_cliques(G):
    if len(c) == 3 and any(n[0] == 't' for n in c):
        three_cliques += 1
    if len(c) > max_clique:
        password = ",".join(sorted(c))
        max_clique = len(c)

print(three_cliques)
print(password)
