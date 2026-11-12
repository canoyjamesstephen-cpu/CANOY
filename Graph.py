from collections import deque


class Graph:
    def __init__(self):
        self.adj = {}  # adjacency list

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        # Undirected graph: connect both ways
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        self.adj[v].append(u)

    # Breadth-First Search using a queue
    def bfs(self, start):
        visited = {start}
        queue = deque([start])
        result = []
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for neighbor in self.adj[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    # Depth-First Search using recursion
    def dfs(self, vertex, visited=None, result=None):
        if visited is None:
            visited = set()
        if result is None:
            result = []
        visited.add(vertex)
        result.append(vertex)
        for neighbor in self.adj[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, result)
        return result

    def display(self):
        for vertex, neighbors in self.adj.items():
            print(f"{vertex}: {', '.join(neighbors)}")


if __name__ == "__main__":
    print("--- GRAPH (CANOY) ---")
    # Graph structure for CANOY:
    #     C --- A --- O
    #     |     |
    #     N --- Y
    g = Graph()
    g.add_edge('C', 'A')
    g.add_edge('C', 'N')
    g.add_edge('A', 'O')
    g.add_edge('A', 'Y')
    g.add_edge('N', 'Y')

    print("Adjacency List:")
    g.display()
    print("BFS Traversal:", " -> ".join(g.bfs('C')))
    print("DFS Traversal:", " -> ".join(g.dfs('C')))