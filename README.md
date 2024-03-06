# Embeddable Grid Graph Generator

Builds an adjacency matrix of a grid like graph that can be naturally embedded
in the selected surface.

size: the length of a side of the square that contains the grid. Defaults to 4 if
provided number is less than 4.

topo: string. Base topology. One of D, T, C, KB, PP, MB, S corresponding to
the standard square grid embedded in the plane (disc), a torus, a cylinder,
a klein bottle, a projective plane, a Moebius band  and a sphere, respectively.
Defaults to D if not provided.

```
import EmbeddableGridGraphClass as egg
AM = egg.EmbeddableGridGraph(4, "T").adjacency_matrix()
```

# Wilsons Spanning Tree generator plus cycles

Builds a spanning tree of any adjacency matrix provided in list of lists format and
adds independently at random a number of edges corresponding to the number of cycles
selected. Said number defaults to zero if not provided and is internally capped at the
maximum number of edges that is possible to add.

```
TREE = wsp.SpanningTreePlusCycles(AM, 4).generate_spanning_tree()
import WilsonSpanningTreePlusLoops as wsp
```
