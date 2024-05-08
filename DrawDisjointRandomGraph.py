import networkx as nx
import matplotlib.pyplot as plt
import random2 as random

def create_tree_graph(vertices_count):
    # Create an empty graph
    G = nx.Graph()
    
    # Add vertices to the graph
    G.add_nodes_from(range(vertices_count))
    
    # Connect half of the vertices randomly
    edges_count = vertices_count // 2
    added_edges = 0
    while added_edges < edges_count:
        # Randomly pick two vertices to connect
        v1, v2 = random.sample(range(vertices_count), 2)
        # Add an edge if it does not exist already
        if not G.has_edge(v1, v2):
            G.add_edge(v1, v2)
            added_edges += 1
    # Draw the graph
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=16, font_color='darkred')
    plt.show()
def main():
    create_tree_graph(10)  # Adjust the number of vertices as needed


if __name__ == '__main__':
    main()