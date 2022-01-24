import random


# vertices/nodes of the graph
class Vertex:

    # value of the vertex will be the word
    def __init__(self, value):
        self.value = value

        # adjacent dictionary to keep track of the vertices that are connected to this one
        # keys = vertices, values = weights of edges
        self.adjacent = {}
        self.neighbors = []
        self.neighbors_weights = []

    # #default weight of 0 if user doesn't add a weight
    def add_edge_to(self, vertex, weight=0):
        # adding an edge to the vertex we input with weight
        self.adjacent[vertex] = weight

    # incrementing the weight of the edge from the current vertex to whatever vertex we give it
    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    # creates a probability map for the vertex
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    # randomly gets the next word from that verted based on weights
    def next_word(self):
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]


# Graph of the vertices
class Graph:

    # initializing an empty dictionary of vertices
    # keys = vertices, values = words
    def __init__(self):
        self.vertices = {}

    # return all words in dictionary
    def get_vertex_values(self):
        return set(self.vertices.keys())

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        # if value isn't in the graph, add it
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]

    # find the next vertex object that corresponds to the current vertex
    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    # get all the probablity mappings of every single vertex
    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()
