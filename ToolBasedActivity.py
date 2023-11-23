import networkx as nx
import matplotlib.pyplot as plt
import random

def generate_library_graph(users, books, edges):
    G = nx.Graph()
    G.add_nodes_from(users, node_type='user')
    G.add_nodes_from(books, node_type='book')
    G.add_edges_from(edges)
    return G

def recommend_books(G, user):
    already_read = set(G.neighbors(user))
    all_books = {node for node, node_type in G.nodes(data='node_type') if node_type == 'book'}

    # Use Inclusion-Exclusion to calculate the set of books not yet read by the user
    recommended_books = all_books - already_read
    for neighbor in G.neighbors(user):
        recommended_books -= set(G.neighbors(neighbor))

    return recommended_books

def visualize_graph(G):
    pos = nx.spring_layout(G)
    node_colors = ['blue' if G.nodes[node]['node_type'] == 'user' else 'green' for node in G.nodes]
    nx.draw(G, pos, with_labels=True, node_color=node_colors)
    plt.show()

# Example data
users = [f'User{i}' for i in range(1, 5)]
books = [f'Book{i}' for i in range(1, 15)]
edges = [(random.choice(users), random.choice(books)) for _ in range(30)]

# Generate the library graph
library_graph = generate_library_graph(users, books, edges)

# Visualize the graph
visualize_graph(library_graph)

# Example: Recommend books for user 'User1'
user_to_recommend = 'User1'
recommended_books = recommend_books(library_graph, user_to_recommend)
print(f"Recommended books for {user_to_recommend}: {recommended_books}")
