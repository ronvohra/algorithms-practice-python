from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topological_sort_helper(self, v, visited, stack):
        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_helper(i, visited, stack)

        # Push current vertex to stack which stores result (if printing dependencies, should this be reverse order?)
        stack.insert(0, v)

    def topological_sort(self):  # has to be a DAG? (no cycles, directed); O(V + E) (linear - sum of vertices and edges)
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological Sort, starting from all vertices one by one
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_helper(i, visited, stack)

        print(stack)

    @staticmethod
    def test_topological_sort():
        g = Graph(6)
        g.add_edge(5, 2)
        g.add_edge(5, 0)
        g.add_edge(4, 0)
        g.add_edge(4, 1)
        g.add_edge(2, 3)
        g.add_edge(3, 1)
        print("Following is a Topological Sort of the given graph")
        g.topological_sort()


if __name__ == "__main__":
    Graph.test_topological_sort()
