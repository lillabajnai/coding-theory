import numpy as np

class ExtendedGolayCode:
    def __init__(self):
        # A kiterjesztett Golay kód generátor mátrixának meghatározása
        self.G = np.array([
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1]
        ])
        self.H = np.array([
            [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1]
        ])

    def encode(self, message):
        """
        A kódszó kódolása a generátor mátrix segítségével.
        """
        if len(message) != 12:
            raise ValueError("Az üzenetnek 12 bit hosszúnak kell lennie.")

        return np.dot(message, self.G) % 2

    def decode(self, received):
        """
        A kódszó dekódolása a szindróma dekódolással.
        """
        # Ellenőrző mátrix
        syndrome = np.dot(received, self.H.T) % 2

        if np.any(syndrome):
            error_position = int("".join(str(x) for x in syndrome[::-1]), 2) - 1
            if 0 <= error_position < len(received):
                received[error_position] ^= 1

        return received[:12]


# if __name__ == "__main__":
    # golay = ExtendedGolayCode()
    # message = [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]  # 12 bit üzenet
    # encoded_message = golay.encode(message)
    # print(f"Encoded message: {encoded_message}")
    #
    # received_message = encoded_message.copy()
    # received_message[5] ^= 1  # Hibát szúrunk be
    # print(f"Received message with error: {received_message}")
    #
    # decoded_message = golay.decode(received_message)
    # print(f"Decoded message: {decoded_message}")
