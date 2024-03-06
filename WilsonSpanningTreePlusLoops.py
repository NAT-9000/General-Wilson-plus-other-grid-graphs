# Random spanning tree generator for grid graphs plus the possible
# addition of cycles.
# author: Natalia Garcia-Colin
"""
Wilson's Algorithm is an algorithm to generate a
uniform spanning tree using a cycle erased random walk. 
In this modification specific for grid graphs I've added the 
possibility of introducing cycles.

Wilson's Algorithm:
1. Choose a random vertex and add it to the visited list.
2. Choose another random vertex (Don’t add to visited list).
   This is the current vertex.
3. Choose a random vertex that is adjacent to the current vertex
   (Don’t add to visited list). This is your new current vertex.
4. Save the edge that you traveled (duple consisting of (previous current, current current)).
5. If the current vertex is not in the visited vertex list:
   a. Go to 3
6. Else:
   a. Starting at the vertex selected in step 2, change the value of the corresponding adjacencies in the 
      adjacency matrix. 
   b. Add all vertices that are passed into the visited list.
7. If all vertices have not been visited
   a. Go to 2
8  Random walk is finished when all vertices have been visited. 
   (A spanning tree is generated)
8. (Adding cycles) Once a random tree has been generated the algorithm adds
cycles by adding 'number of cycles' edges independently at random.
"""""
import random

class SpanningTreePlusCycles:

    def __init__(self, adjacency_matrix, number_of_cycles = 0):

        self.original_adjacency_matrix = adjacency_matrix
        self.number_of_vertices = len(self.original_adjacency_matrix[0])
        self.number_of_cycles = number_of_cycles
        # declare instance variable
        self.visited = []  # visited vertices
        self.unvisited = []  # unvisited vertices
        self.path = dict()
        # adjacency matrix of grid graph initialized with zero values
        self.tree_adjacency_matrix = [[0 for _ in range(self.number_of_vertices)] for _ in range(self.number_of_vertices)]

    def generate_spanning_tree(self):
        """WilsonGridGraphGeneratorWCycles.generate_spanningTree() -> None
        Generates the spanning tree according to the Wilson Loop Erased Random
        Walk Algorithm and adds pi edges independently at random"""
        # reset list of unvisited vertices
        self.unvisited = list(range(0, self.number_of_vertices))

        # choose the first vertex to put in the visited list (Step 1)
        current = self.unvisited.pop(random.randint(0, len(self.unvisited) - 1))
        self.visited.append(current)

        # loop until all vertices have been visited
        while len(self.unvisited) > 0:
            # choose a random vertex to start the walk (Step 2)
            first = self.unvisited[random.randint(0, len(self.unvisited) - 1)]
            current = first
            # loop until the random walk reaches a visited vertex
            while True:
                # choose randomly a new neighbouring vertex (Step 3)
                adjacent_vertices = [i for i, val in enumerate(self.original_adjacency_matrix[current]) if val != 0]
                next_vertex = random.choice(adjacent_vertices)
                # save the next_vertex in a preliminary path dictionary.
                self.path[current] = next_vertex
                current = next_vertex
                # check if the vertex has already been visited
                if current in self.visited:  # visited cell is reached (Step 5)
                    break

            # Record the preliminary path and adjacency matrix of the partial spanning tree
            current = first  # go to start of preliminary path
            # loop until the end of preliminary path is reached
            while True:
                # add vertex to visited list, remove vertex from unvisited list
                self.visited.append(current)
                self.unvisited.remove(current)  # (Step 6.b)
                # mark adjacency in adjacency matrix.
                self.tree_adjacency_matrix[current][self.path[current]] = 1
                self.tree_adjacency_matrix[self.path[current]][current] = 1
                # go to next vertex (Step 6.a)
                current = self.path[current]

                if current in self.visited:  # end of path is reached
                    self.path = dict()  # clear the path
                    break

        # # add cycles
        # Calculating the maximum number of edges that is possible to add.
        self.max_cycles = self.underlying_graph_edge_count() - (self.number_of_vertices - 1)

        if self.number_of_cycles != 0:
            # Capping the number of edges at maximum.
            self.number_of_cycles = min (self.max_cycles, self.number_of_cycles)
            for i in range(self.number_of_cycles):
                while True:
                    # select a random edge
                    r = random.randint(0, self.number_of_vertices - 1)
                    c = random.randint(0, self.number_of_vertices - 1)

                    if r != c: # check that is not trying to add a self-loop
                        if self.tree_adjacency_matrix[r][c] == 0:
                            # mark adjacency matrix
                            self.tree_adjacency_matrix[r][c] = 1
                            self.tree_adjacency_matrix[c][r] = 1
                            break
        return self.tree_adjacency_matrix

    # Counts the number of edges of the final random spanning tree plus cycles.
    def final_edge_count(self):
        n = 0
        for r in range(0, self.number_of_vertices):
            n = n + self.tree_adjacency_matrix[r].count(1)

        return n // 2

    # Counts the number of edges of the underlying grid graph.
    def underlying_graph_edge_count(self):
        n = 0
        for r in range(0, self.number_of_vertices):
            n = n + self.original_adjacency_matrix[r].count(1)

        return n // 2

