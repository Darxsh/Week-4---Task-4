from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    # Add edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # A recursive function to perform DFS
    def dfs(self, v, visited, stack=None):
        visited[v] = True
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                self.dfs(neighbour, visited, stack)
        if stack is not None:
            stack.append(v)

    # Function to transpose the graph
    def transpose(self):
        transposed_graph = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                transposed_graph.add_edge(v, u)
        return transposed_graph

    # The main function to find and print all SCCs
    def find_sccs(self):
        # Step 1: Fill vertices in stack according to their finishing times
        stack = []
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        # Step 2: Transpose the graph
        transposed_graph = self.transpose()

        # Step 3: Process all vertices in order defined by the stack
        visited = [False] * self.V
        sccs = []
        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                transposed_graph.dfs(v, visited, component)
                sccs.append(component)

        return sccs

# Example Usage:
g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)

sccs = g.find_sccs()
print("Strongly Connected Components:", sccs)
