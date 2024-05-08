import random
import networkx as nx
import matplotlib.pyplot as plt

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return False
        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1
        return True

def draw_connected_graph(n):
    """Generate a graph with n nodes and draw it once it becomes connected."""
    G = nx.Graph()
    G.add_nodes_from(range(n))
    uf = UnionFind(n)
    edges = [(i, j) for i in range(n) for j in range(i+1, n)]
    random.shuffle(edges)

    for u, v in edges:
        if uf.union(u, v):
            G.add_edge(u, v)
            if len(set(uf.find(i) for i in range(n))) == 1:
                # The graph is now connected
                break

    # Draw the graph
    plt.figure(figsize=(8, 5))
    nx.draw(G, with_labels=True, node_color='lightblue')
    plt.title(f'Connected Graph with {n} Nodes')
    plt.show()

def main():
    ns = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    for n in ns:
        draw_connected_graph(n)

if __name__ == "__main__":
    main()
