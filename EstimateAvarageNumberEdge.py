import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

def estimate_average_edges(n, iter):
    total_edges = 0
    
    for _ in range(iter):
        G = nx.Graph()
        G.add_nodes_from(range(n))
        edges_count = 0
        
        # Continue until the graph is connected
        while not nx.is_connected(G):
            #print(G.nodes())
            list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  

            a, b = random.sample(list(G.nodes()), 2)
            if not G.has_edge(a, b):
                G.add_edge(a, b)
                edges_count += 1
        
        total_edges += edges_count
    
    average_edges = total_edges / iter
    return average_edges, G

def plot_graph(G):
    # Draw the graph
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold', font_color='darkred')
    plt.title("Example of a Connected Graph")
    plt.show()

n = 10  # Number of vertices
iter = 100  # Number of iterations
def main():

    average_edges, result_graph = estimate_average_edges(n, iter)

    # Print the estimated average number of edges
    print(f"Estimated average number of edges required to connect a graph with {n} vertices: {average_edges}")

    # Display the graph from the last iteration
    plot_graph(result_graph)

if __name__ == '__main__':
    main()