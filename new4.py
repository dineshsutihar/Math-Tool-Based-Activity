from collections import defaultdict
from itertools import combinations

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

class LibraryBookRecommendation:
    def __init__(self, graph):
        self.graph = graph
        self.users = set()
        self.books = set()
        self.user_books = defaultdict(set)
        self.book_genres = defaultdict(list)

    def identify_reading_communities(self):
        communities = []
        for u in self.users:
            for v in self.users:
                if v in self.graph.graph[u]:
                    communities.append((u, v))
        return communities

    def avoid_recommendations_for_already_read_books(self):
        recommended_books = self.books.copy()
        for k in range(1, len(self.users) + 1):
            for users in combinations(self.users, k):
                already_read = set.intersection(*(self.user_books[user] for user in users))
                recommended_books -= already_read
        return recommended_books

    def analyze_book_genres_distribution(self):
        G = defaultdict(int)
        for book in self.books:
            for genre in self.book_genres[book]:
                G[genre] += 1
        return G

    def real_time_adaptation(self, recommended_books, user_feedback, adaptation_rate):
        R_n = list(recommended_books)
        for n in range(len(R_n)):
            R_n[n] = R_n[n] + adaptation_rate * (user_feedback[n] - R_n[n])
        return R_n