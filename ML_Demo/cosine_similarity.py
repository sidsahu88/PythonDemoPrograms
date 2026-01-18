import numpy as np

def cosine_similarity(vec_a, vec_b):
    """Calculate the cosine similarity between two vectors.
        Cosine similarity is defined as the dot product of the vectors
        divided by the product of their magnitudes.
    """
    dot_product = np.dot(vec_a, vec_b)
    squared_a = vec_a**2
    squared_b = vec_b**2
    magnitude_a = np.sqrt(np.sum(squared_a))
    magnitude_b = np.sqrt(np.sum(squared_b))
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0
    return dot_product / (magnitude_a * magnitude_b)


if __name__ == "__main__":
    vec1 = np.array([0.9, 0.88, 0.12, 0.45, 0.21, 0.67])
    vec2 = np.array([0.8, 0.96, 0.2, 0.39, 0.18, 0.75])
    vec3 = np.array([0.1, 0.24, 0.88, 0.55, 0.79, 0.33])
    similarity_12 = cosine_similarity(vec1, vec2)
    similarity_13 = cosine_similarity(vec1, vec3)
    similarity_23 = cosine_similarity(vec2, vec3)
    print(f"Cosine Similarity between vec1 and vec2: {similarity_12}")
    print(f"Cosine Similarity between vec1 and vec3: {similarity_13}")
    print(f"Cosine Similarity between vec2 and vec3: {similarity_23}")