import networkx as nx
import matplotlib.pyplot as plt

def count_isolated_vertices(G):
    """
    Counts the isolated vertices in a graph and visualizes the graph with isolated vertices highlighted.

    Parameters:
    G (nx.Graph): The graph to analyze and visualize.

    Returns:
    int: The number of isolated vertices.
    """
    isolated_nodes = [node for node in G.nodes if G.degree(node) == 0]
    isolated_count = len(isolated_nodes)
    
    # Setting up colors for the visualization: isolated vertices in red, others in blue
    node_colors = ['red' if node in isolated_nodes else 'blue' for node in G.nodes]
    
    return isolated_count,G
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
# Example usage:
if __name__ == "__main__":
    G = nx.Graph()
    G.add_nodes_from(range(10))  # Add 10 nodes
    G.add_edges_from([(0, 1), (2, 3), (4, 5), (5, 6)])  # Adding some edges

    # Count isolated vertices and visualize the graph

    isolated_count, Gx = count_isolated_vertices(G)
    print(f"Total isolated vertices: {isolated_count}")
    highlight_isolated_vertices(Gx)
