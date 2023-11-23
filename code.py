import networkx as nx
import matplotlib.pyplot as plt
import random
# Function to generate a random graph with users and books
def generate_library_graph(users, books, edges):
    G = nx.Graph()

    # Adding nodes (users and books)
    G.add_nodes_from(users, node_type='user')
    G.add_nodes_from(books, node_type='book')

    # Adding edges based on user-book interactions
    G.add_edges_from(edges)

    return G
# Function to recommend books using the Inclusion-Exclusion Principle
def recommend_books(G, user):
    already_read = set(G.neighbors(user))

    # Calculate the set of all books
    all_books = set(book for book, node_type in G.nodes(data='node_type') if node_type == 'book')

    # Calculate the set of books not yet read by the user using Inclusion-Exclusion
    recommended_books = all_books - already_read

    return recommended_books
# Function to visualize the graph
def visualize_graph(G):
    pos = nx.spring_layout(G)
    node_colors = ['blue' if G.nodes[node]['node_type'] == 'user' else 'green' for node in G.nodes]

    nx.draw(G, pos, with_labels=True, node_color=node_colors)
    plt.show()
# Example data
users = ['Rahul', 'Amit', 'Priya', 'Sneha']
books = ['The Guide', 'The God of Small Things', 'Shiva Trilogy', 'The Namesake']
edges = [('Rahul', 'The Guide'), ('Rahul', 'The God of Small Things'),
         ('Amit', 'Shiva Trilogy'), ('Priya', 'The Namesake'), ('Sneha', 'The Guide')]

# Generate the library graph
library_graph = generate_library_graph(users, books, edges)

# Visualize the graph
visualize_graph(library_graph)

# Example: Recommend books for user 'Rahul'
user_to_recommend = 'Amit'
recommended_books = recommend_books(library_graph, user_to_recommend)

print(f"Recommended books for {user_to_recommend}: {recommended_books}")
