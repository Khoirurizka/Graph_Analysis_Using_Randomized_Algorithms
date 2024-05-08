import networkx as nx
import matplotlib.pyplot as plt
import random

def create_graph(n, edge_prob):
    """
    Creates a graph with n vertices, where each pair of vertices has a chance (edge_prob)
    of being connected by an edge.
    """
    G = nx.Graph()
    G.add_nodes_from(range(n))
    
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < edge_prob:
                G.add_edge(i, j)

    return G

def highlight_isolated_vertices(G):
    """
    Draws the graph and highlights isolated vertices in red.
    """
    # Determine isolated nodes
    isolated_nodes = [node for node in G.nodes if G.degree(node) == 0]
    node_colors = ['red' if node in isolated_nodes else 'lightblue' for node in G.nodes]

    # Draw the graph
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, font_weight='bold', font_color='darkred')
    plt.title("Graph with Isolated Vertices Highlighted")
    plt.show()

def main():
    n = 10  # Number of vertices
    edge_prob = 0.3  # Probability of creating an edge between two vertices

    G = create_graph(n, edge_prob)
    highlight_isolated_vertices(G)

if __name__ == '__main__':
    main()
