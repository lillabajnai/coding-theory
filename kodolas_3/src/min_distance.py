import numpy as np

def hamming_distance(u, v):
    """
    létrehoz egy olyan listát, ahol minden elem egy (c1, c2) pár, ahol c1 a-ból, c2 pedig b-ből származik.
    logikai értéket ad minden egyes párra, attól függően, hogy a két karakter egyenlő-e
    megszámolja, hogy hány darab True érték van a listában, azaz hány helyen különböznek a karakterek
    """
    return sum(c1 != c2 for c1, c2 in zip(u, v))

def min_distance(codewords):
    """
    A minimális távolság meghatározása a kódszavak között.
    """
    min_dist = float('inf')
    n = len(codewords)

    for i in range(n):
        for j in range(i + 1, n):
            dist = hamming_distance(codewords[i], codewords[j])
            min_dist = min(min_dist, dist)

    return min_dist

# Példa használat
if __name__ == "__main__":
    G = np.array([[1, 0, 0, 1, 1, 0, 1],
                  [0, 1, 0, 1, 0, 1, 1],
                  [0, 0, 1, 0, 1, 1, 1]])

    print(min_distance(G))  # Minimális távolság
