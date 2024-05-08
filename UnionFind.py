import random
import networkx as nx
import numpy as np

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

def experiment(n):
    """Run one experiment to find the number of edges to connect a graph of size n."""
    uf = UnionFind(n)
    edges = list(nx.complete_graph(n).edges())
    random.shuffle(edges)
    num_edges_added = 0

    for u, v in edges:
        if uf.union(u, v):
            num_edges_added += 1
            if uf.find(0) == uf.find(n - 1):  # A simple check if all nodes are connected
                if len(set(uf.find(i) for i in range(n))) == 1:
                    break
    return num_edges_added

def main():
    ns = range(100, 1001, 100)
    trials = 100
    results = {}

    for n in ns:
        print(f"Running simulations for n = {n}")
        results[n] = np.mean([experiment(n) for _ in range(trials)])

    for n in sorted(results):
        print(f"Average number of edges needed for n = {n}: {results[n]:.2f}")

if __name__ == "__main__":
    main()
