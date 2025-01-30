import numpy as np

def syndrome_decode(H, received):
    """
       Szindróma dekódolás: Az adott H mátrix és input kódszó alapján javítja a hibát, ha szükséges, és visszaadja a dekódolt üzenetet.

       received_copy (numpy array): A javított kódszó, ha szükséges.
       error_position (int or None): A hiba pozíciója (1-indexelt), ha hiba történt, különben None.
       """
    syndrome = np.dot(H, received) % 2
    if not np.any(syndrome):
        return received, None

    error_position = None
    received_copy = received.copy()
    for i in range(H.shape[1]):
        if np.array_equal(H[:, i], syndrome):
            received_copy[i] = 1 - received_copy[i]
            error_position = i + 1
            break
    return received_copy, error_position

if __name__ == "__main__":
    H = np.array([[1, 0, 0, 0, 0, 1, 1],
                  [0, 1, 0, 0, 1, 0, 1],
                  [0, 0, 1, 0, 1, 1, 0],
                  [0, 0, 0, 1, 1, 1, 1]])

    received = np.array([1, 1, 1, 0, 1, 0, 1])  # hibás kódszó
    decoded, error_position = syndrome_decode(H, received)
    print(f"Dekódolt üzenet: {decoded}")
    if error_position:
        print(f"Hiba a {error_position}. biten volt.")
    else:
        print("Nincs hiba.")
