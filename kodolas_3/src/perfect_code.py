import numpy as np
from scipy.special import comb

from src.min_distance import min_distance


def hamming_sphere_size(n, t, p):
    """
    Kiszámítja a Hamming-gömb méretét az adott sugarú t és n hosszúságú szavak felett p számrendszerben.
    """
    return sum(comb(n, i, exact=True) * (p - 1) ** i for i in range(t + 1))


def is_perfect_code(G, p):
    """
    Ellenőrzi, hogy egy generátor mátrix által létrehozott kód tökéletes kód-e.
    Egy kód tökéletes, ha a kódszavak Hamming-távolsága elég nagy ahhoz, hogy minden lehetséges hibás kódszóval elkerülhető legyen a dekódolás során

    Paraméterek:
        G: np.array, a generátor mátrix (k x n méretű)
        p: a test mérete
    """
    k, n = G.shape
    M = p ** k   # kódszavak száma
    T = p ** n   # lehetséges kódszavak teljes száma

    # Az összes kódszó generálása (minden lehetséges bináris bemenet)
    codewords = [np.dot(m, G) % p for m in np.array(np.meshgrid(*[range(p)] * k)).T.reshape(-1, k)]

    d = min_distance(codewords)

    t = (d - 1) // 2
    S = hamming_sphere_size(n, t, p)

    return M * S == T


if __name__ == "__main__":
    G_hamming = np.array([
        [1, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1]
    ])

    # ---- Teszteljük a tökéletességet ----
    is_perfect = is_perfect_code(G_hamming, p=2)
    print(f"A (7,4) Hamming-kód tökéletes? {is_perfect}") # True