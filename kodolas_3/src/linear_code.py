import numpy as np

from src.zp import Zp

class LinearCode:
    def __init__(self, G, p):
        self.G = np.array(G)
        self.zp = Zp(p)

    def encode(self, message):
        """
            Kódolja az üzenetet a generátor mátrix (G) segítségével.
        """
        encoded_message = self.zp.mat_mul([message], self.G)
        return encoded_message[0]

if __name__ == "__main__":
    G = [[1, 0, 0, 1, 1, 0, 1],
         [0, 1, 0, 1, 0, 1, 1],
         [0, 0, 1, 0, 1, 1, 1]]

    code = LinearCode(G, 2)
    message = [1, 0, 1]
    print(code.encode(message))
