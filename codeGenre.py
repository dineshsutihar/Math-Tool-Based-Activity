import networkx as nx
import matplotlib.pyplot as plt
import random

def generate_library_graph(users, books, edges, genres):
    G = nx.Graph()
    G.add_nodes_from(users, node_type='user')
    G.add_nodes_from(books, node_type='book')

    # Adding genre information to the graph
    for book in books:
        genre = genres.get(book, 'Unknown')  # Default to 'Unknown' if genre not specified
        G.nodes[book]['genre'] = genre

    G.add_edges_from(edges)

    return G

def recommend_books(G, user):
    already_read = set(G.neighbors(user))

    # Calculate the set of all books
    all_books = {node for node, node_type in G.nodes(data='node_type') if node_type == 'book'}

    # Calculate the set of books not yet read by the user using Inclusion-Exclusion
    recommended_books = all_books - already_read

    # Consider genres in recommendations
    user_genre_preferences = set(G.nodes[user].get('genre', 'Unknown'))  # Default to 'Unknown' if genre not specified
    recommended_books = {book for book in recommended_books if G.nodes[book].get('genre', 'Unknown') in user_genre_preferences}

    return recommended_books

def visualize_graph(G):
    pos = nx.spring_layout(G)
    node_colors = ['blue' if G.nodes[node]['node_type'] == 'user' else 'green' for node in G.nodes]
    nx.draw(G, pos, with_labels=True, node_color=node_colors)
    plt.show()

def generate_genre_distribution():
    # Generating Functions: Define a simple generating function for illustration purposes.
    genres = ['Fiction', 'Mystery', 'Romance', 'Science Fiction']
    genre_distribution = {genre: random.randint(1, 10) for genre in genres}
    return genre_distribution

def real_time_adaptation(recommendations, user_feedback, adaptation_rate=0.1):
    updated_recommendations = set(recommendations)  # Ensure recommendations is a set
    new_books = {book for book in user_feedback if book not in recommendations}
    updated_recommendations = updated_recommendations.union(new_books)
    updated_recommendations = updated_recommendations.union(
        {book for book in user_feedback if random.random() < adaptation_rate}
    )
    return updated_recommendations

# Example data
users = [f'User{i}' for i in range(1, 5)]
books = [f'Book{i}' for i in range(1, 15)]
genres = {f'Book{i}': random.choice(['Fiction', 'Mystery', 'Romance', 'Science Fiction']) for i in range(1, 15)}
edges = [(random.choice(users), random.choice(books)) for _ in range(30)]

# Generate the library graph
library_graph = generate_library_graph(users, books, edges, genres)

# Visualize the graph
visualize_graph(library_graph)

# Example: Recommend books for user 'User1'
user_to_recommend = 'User1'
recommended_books = recommend_books(library_graph, user_to_recommend)

# Generating Functions: Analyze the distribution of book genres.
genre_distribution = generate_genre_distribution()
print(f"Book Genre Distribution: {genre_distribution}")

# Real-time Adaptation: Simulate real-time adaptation based on user feedback.
user_feedback = {random.choice(books), random.choice(books)}
updated_recommendations = real_time_adaptation(recommended_books, user_feedback)
print(f"Updated Recommendations after User Feedback: {updated_recommendations}")
