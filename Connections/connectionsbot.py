import spacy

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from itertools import combinations

nlp = spacy.load('en_core_web_md')


def get_word_vector(word):
    return nlp(word).vector

def get_similarity(word1, word2):
    return nlp(word1).similarity(nlp(word2))

def score_cluster(cluster): 
    pairwise_similarities = [get_similarity(word1, word2) for word1, word2 in combinations(cluster, 2)]
    return np.mean(pairwise_similarities)


def cluster_words(words, n_clusters=4):
    embeddings = np.array([get_word_vector(word) for word in words])

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(embeddings)

    clusters = {i: [] for i in range(n_clusters)}
    for word, label in zip(words, labels):
        clusters[label].append(word)

    cluster_list = list(clusters.values())
    if not all(len(cluster) == 4 for cluster in cluster_list):
        print("Warning: Uneven clusters, results may be inaccurate.")


    cluster_scores = {tuple(cluster): score_cluster(cluster) for cluster in cluster_list}
    best_guess = max(cluster_scores, key=cluster_scores.get)

    return cluster_list, best_guess
def is_valid_guess(guess, words):
    if len(set(guess)) != 4:
        return False
    if not all(word in words for word in guess):
        return False
    return True

def word_combinations(words):
    return set([combo for combo in combinations(words, 4)])


words = [
    "butte", "china", "hearth", "shine", # BODY PARTS + A LETTER
    "gobble", "gulp", "scarf", "wolf",   # EAT VIGOROUSLY
    "bow", "buckle", "cave", "give",     # bend under weight 
    "anchor", "compass", "mermaid", "swallow" # classic nautical tattoos
]

# Run clustering and get best first guess
# clusters, best_guess = cluster_words(words)

# # Print results
# for idx, cluster in enumerate(clusters, 1):
#     print(f"Group {idx}: {cluster}")

# print("\nBest First Guess:", best_guess)
combs_array = word_combinations(words)

# Store (word, score) pairs
best_guesses = []

for word in combs_array:
    best_guesses.append((word, score_cluster(word)))

# Sort by score in descending order
best_guesses.sort(key=lambda x: x[1], reverse=True)

# Print the top 10 words
for word, score in best_guesses[:10]:
    print(word)



