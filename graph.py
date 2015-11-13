# Implementation of a basic graph representation
# By: Jacob Rockland

from collections import defaultdict

# implementation of graph class
class Graph(object):

    # graph initialization
    def __init__(self, connections = None, directed = False):
        self.graph = defaultdict(set)
        self.directed = directed
        if connections is not None:
            self.add_connections(connections)

    # add vertex to graph
    def add_vertex(self, vertex):
        self.graph[vertex] = set()

    # adds graph connection between vertex and adjacent vertex
    def add_connection(self, vertex, adjacent):
        self.graph[vertex].add(adjacent)
        if not self.directed:
            self.graph[adjacent].add(vertex)

    # adds iterable of tuple pairs representing connections to graph
    def add_connections(self, connections):
        for vertex, adjacent in connections:
            self.add_connection(vertex, adjacent)

    # removes a given vertex from graph
    def remove_vertex(self, vertex):
        for adjacencies in self.graph.itervalues():
            if vertex in adjacencies:
                adjacencies.remove(vertex)
        if vertex in self.graph:
            del self.graph[vertex]

    # removes graph connection between vertex and adjacent vertex
    def remove_connection(self, vertex, adjacent):
        if adjacent in self.graph[vertex]:
            self.graph[vertex].remove(adjacent)
        if not self.directed:
            if vertex in self.graph[adjacent]:
                self.graph[adjacent].remove(vertex)

    # removes iterable of tuple pairs representing connections to graph
    def remove_connections(self, connections):
        for vertex, adjacent in connections:
            self.remove_connection(vertex, adjacent)

    # returns boolean value signifying whether or not two nodes are connected
    def connected(self, vertex, adjacent):
        if vertex in self.graph and adjacent in self.graph[vertex]:
            return True
        elif not self.directed:
            if adjacent in self.graph and vertex in self.graph[adjacent]:
                return True
        return False

    # breadth first search implementation
    def bfs(self, start):
        discovered = set()
        queue = [start]
        while queue:
            current = queue.pop(0)
            for adjacent in self.graph[current]:
                if adjacent not in discovered:
                    discovered.add(adjacent)
                    queue.append(adjacent)
        return discovered
