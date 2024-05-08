import networkx as nx
import matplotlib.pyplot as plt
import random

def estimate_average_edges(n, iter):
    total_edges_g = 0
    total_edges_f = 0
    
    for _ in range(iter):
        G = nx.Graph()
        G.add_nodes_from(range(n))
        edges_count_g = 0
        edges_count_f = 0
        
        while not nx.is_connected(G):
            
            
            a, b = random.sample(list(G.nodes()), 2)
            if not G.has_edge(a, b):
                G.add_edge(a, b)

                isolated_nodes = [node for node in G.nodes if G.degree(node) == 0]
                isolated_count = len(isolated_nodes)
                if isolated_count>0:
                    edges_count_g += 1

                edges_count_f += 1

                
        total_edges_g += edges_count_g  # Snapshot of edges when no isolated vertices remain
        total_edges_f += edges_count_f  # Total edges to connect the graph
    
    average_edges_g = total_edges_g / iter
    average_edges_f = total_edges_f / iter
    return average_edges_g, average_edges_f, G

def plot_graph(G):
    # Determine isolated nodes for highlighting
    isolated_nodes = [node for node in G.nodes if G.degree(node) == 0]
    node_colors = ['red' if node in isolated_nodes else 'lightblue' for node in G.nodes]

    # Draw the graph with isolated nodes highlighted in red
    nx.draw(G, with_labels=True, node_color=node_colors, node_size=500, font_weight='bold', font_color='darkred')
    plt.title("Final Graph Example with Isolated Vertices Highlighted")
    plt.show()

n = 1000  # Number of vertices
iter = 100  # Number of iterations

def main():
    average_edges_g, average_edges_f, result_graph = estimate_average_edges(n, iter)
    print(f"Estimated average number of edges required to connect the graph (f(n)): {average_edges_f}")
    print(f"Estimated average number of edges required to eliminate isolated vertices (g(n)): {average_edges_g}")
    plot_graph(result_graph)

if __name__ == '__main__':
    main()
