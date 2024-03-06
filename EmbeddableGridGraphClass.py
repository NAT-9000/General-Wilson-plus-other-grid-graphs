class EmbeddableGridGraph:
    """Grid graph adjacency matrix generator """

    def __init__(self, size=4, topo="D"):
        """EmbeddableGridGraph(self, int, str) -> adjacency_matrix
        Creates the adjacency matrix of a grid graph of the given size embedded in
        the given surface.
        size: the length of a side of the square that contains the grid
        topo: string. Base topology. One of D, T, C, KB, PP, MB, S corresponding to
        the standard square grid embedded in the plane (disc), a torus, a cylinder, a klein bottle,
        a projective plane, a Moebius band  and a sphere, respectively. Defaults to D if not provided"""

        self.vertices = size * size
        self.topo = topo
        self.size = size
        # adjacency matrix of grid graph initialized with zero values
        self.adjacency = [[0 for j in range(self.vertices)] for i in range(self.vertices)]

    def adjacency_matrix(self):
        # We first build the standard adjacency matrix for the graph of a square grid of the given size.
        self.make_adjacency_square_grid()

        # We now deal with the seams.
        # We will first deal with the vertical seam. That is when c = self.size - 1 and/or c = 0.
        for r in range(self.size):
            if self.topo == "D":
                pass
            elif self.topo == "C" or self.topo == "T" or self.topo == "KB" or self.topo == "S":
                vertex_index_in_am = r * self.size + self.size - 1
                right_vertex_index_in_am = r * self.size
                self.adjacency[vertex_index_in_am][right_vertex_index_in_am] = 1
                self.adjacency[right_vertex_index_in_am][vertex_index_in_am] = 1
            elif self.topo == "PP" or self.topo == "MB":
                vertex_index_in_am = r * self.size + self.size - 1
                right_vertex_index_in_am = (self.size - 1 - r) * self.size
                self.adjacency[vertex_index_in_am][right_vertex_index_in_am] = 1
                self.adjacency[right_vertex_index_in_am][vertex_index_in_am] = 1

        # We will now deal with the horizontal seam. That is when r = self.size - 1 and/or r = 0 .
        # Increase the size of the matrix only in the case where topo=="S"
        if self.topo == "S":
            # First we add two rows of zeros to the matrix
            self.adjacency.append([0 for _ in range(self.vertices)])
            self.adjacency.append([0 for _ in range(self.vertices)])

            # then we add two zeros to each row
            for r in range(self.vertices + 2):
                self.adjacency[r].append(0)
                self.adjacency[r].append(0)

        for c in range(self.size):
            if self.topo == "D" or self.topo == "C" or self.topo == "MB":
                pass
            elif self.topo == "T":
                vertex_index_in_am = (self.size - 1) * self.size + c
                down_vertex_index_in_am = c
                self.adjacency[vertex_index_in_am][down_vertex_index_in_am] = 1
                self.adjacency[down_vertex_index_in_am][vertex_index_in_am] = 1
            elif self.topo == "KB" or self.topo == "PP":
                vertex_index_in_am = (self.size - 1) * self.size + c
                down_vertex_index_in_am = self.size - 1 - c
                self.adjacency[vertex_index_in_am][down_vertex_index_in_am] = 1
                self.adjacency[down_vertex_index_in_am][vertex_index_in_am] = 1
            elif self.topo == "S":
                # In this particular case we will add two vertices, the north and south poles
                # First we join all vertices in the first row to the North Pole.
                vertex_index_in_am = c
                up_vertex_index_in_am = self.size * self.size
                self.adjacency[vertex_index_in_am][up_vertex_index_in_am] = 1
                self.adjacency[up_vertex_index_in_am][vertex_index_in_am] = 1
                # Then we join all vertices in the last row to the South Pole.
                vertex_index_in_am = (self.size - 1) * self.size + c
                down_vertex_index_in_am = self.size * self.size + 1
                self.adjacency[vertex_index_in_am][down_vertex_index_in_am] = 1
                self.adjacency[down_vertex_index_in_am][vertex_index_in_am] = 1

        return self.adjacency

    def make_adjacency_square_grid(self):
        # In order to generate the grid we will think of each vertex labelled as (r,c)
        # and given a vertex we will first add the adjacencies to the vertex (r, c+1)
        # and then add adjacencies to its vertex (r+1, c), when possible.
        for r in range(self.size):
            for c in range(self.size):
                vertex_index_in_am = r * self.size + c  # corresponding element in adjacency matrix.
                # We first mark all down and right adjacencies for vertices not in the boundary of
                # the fundamental region
                if c < self.size - 1 and r < self.size - 1:
                    right_vertex_index_in_am = r * self.size + c + 1
                    down_vertex_index_in_am = (r + 1) * self.size + c
                    self.adjacency[vertex_index_in_am][right_vertex_index_in_am] = 1
                    self.adjacency[right_vertex_index_in_am][vertex_index_in_am] = 1
                    self.adjacency[vertex_index_in_am][down_vertex_index_in_am] = 1
                    self.adjacency[down_vertex_index_in_am][vertex_index_in_am] = 1
                # We now add all edges still in the fundamental region but either in the horizontal
                # or vertical edge
                elif c == self.size - 1 and r < self.size - 1:
                    down_vertex_index_in_am = (r + 1) * self.size + c
                    self.adjacency[vertex_index_in_am][down_vertex_index_in_am] = 1
                    self.adjacency[down_vertex_index_in_am][vertex_index_in_am] = 1
                elif c < self.size - 1 and r == self.size - 1:
                    right_vertex_index_in_am = r * self.size + c + 1
                    self.adjacency[vertex_index_in_am][right_vertex_index_in_am] = 1
                    self.adjacency[right_vertex_index_in_am][vertex_index_in_am] = 1
                else:
                    pass


### END OF CODE ###
# EGG = EmbeddedGridGraph(5, "S")
# print(EGG.adjacency_matrix())

