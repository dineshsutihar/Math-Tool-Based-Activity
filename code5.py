import networkx as nx
import matplotlib.pyplot as plt
import random

def generate_library_graph(users, books, edges):
    """
    Generate a random graph with users and books.

    Parameters:
    - users (list): List of user names.
    - books (list): List of book names.
    - edges (list): List of tuples representing user-book interactions.

    Returns:
    - nx.Graph: Generated graph.
    """
    G = nx.Graph()
    G.add_nodes_from(users, node_type='user')
    G.add_nodes_from(books, node_type='book')
    G.add_edges_from(edges)
    return G

def recommend_books(G, user):
    """
    Recommend books to a user using the Inclusion-Exclusion Principle.

    Parameters:
    - G (nx.Graph): Graph representing user-book interactions.
    - user (str): User for whom books are recommended.

    Returns:
    - set: Recommended books.
    """
    already_read = set(G.neighbors(user))
    all_books = {node for node, node_type in G.nodes(data='node_type') if node_type == 'book'}
    recommended_books = all_books - already_read
    return recommended_books

def visualize_graph(G):
    """
    Visualize the graph.

    Parameters:
    - G (nx.Graph): Graph to visualize.
    """
    pos = nx.spring_layout(G)
    node_colors = ['blue' if G.nodes[node]['node_type'] == 'user' else 'green' for node in G.nodes]
    nx.draw(G, pos, with_labels=True, node_color=node_colors)
    plt.show()

def generate_genre_distribution():
    """
    Generate a distribution of book genres using a generating function.

    Returns:
    - dict: Distribution of book genres.
    """
    # Generating Functions: Define a simple generating function for illustration purposes.
    genres = ['Fiction', 'Mystery', 'Romance', 'Science Fiction']
    genre_distribution = {genre: random.randint(1, 10) for genre in genres}
    return genre_distribution

def real_time_adaptation(recommendations, user_feedback, adaptation_rate=0.1):
    """
    Implement real-time adaptation using a recurrence relation.

    Parameters:
    - recommendations (set): Current list of recommended books.
    - user_feedback (set): User feedback on the recommended books.
    - adaptation_rate (float): Rate of adaptation.

    Returns:
    - set: Updated list of recommended books.
    """
    # Recurrence Relations: Update recommendations based on user feedback.
    updated_recommendations = recommendations.union(user_feedback)
    updated_recommendations = recommendations.union(
        {book for book in user_feedback if random.random() < adaptation_rate}
    )
    return updated_recommendations

# Example data
users = ['Rahul', 'Amit', 'Priya', 'Sneha']
books = ['The Guide', 'The God of Small Things', 'Shiva Trilogy', 'The Namesake']
edges = [('Rahul', 'The Guide'), ('Rahul', 'The God of Small Things'),
         ('Amit', 'Shiva Trilogy'), ('Priya', 'The Namesake'), ('Sneha', 'The Guide')]

# Generate the library graph
library_graph = generate_library_graph(users, books, edges)

# Visualize the graph
visualize_graph(library_graph)

# Example: Recommend books for user 'Amit'
user_to_recommend = 'Amit'
recommended_books = recommend_books(library_graph, user_to_recommend)

# Generating Functions: Analyze the distribution of book genres.
genre_distribution = generate_genre_distribution()
print(f"Book Genre Distribution: {genre_distribution}")

# Real-time Adaptation: Simulate real-time adaptation based on user feedback.
user_feedback = {'The God of Small Things', 'The Namesake'}
updated_recommendations = real_time_adaptation(recommended_books, user_feedback)
print(f"Updated Recommendations after User Feedback: {updated_recommendations}")
