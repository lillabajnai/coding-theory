import numpy as np


class Zp:
    def __init__(self, p):
        assert self.is_prime(p), "p should be a prime number."
        self.p = p

    def add(self, a, b):
        return (a % self.p + b % self.p) % self.p

    def sub(self, a, b):
        return (a % self.p - b % self.p) % self.p

    def mul(self, a, b):
        return (a % self.p * b % self.p) % self.p

    def inv(self, a):
        if a == 0:
            raise ValueError("0 has no multiplicative inverse in Z_p")
        return pow(a, self.p - 2, self.p)

    def div(self, a, b):
        return self.mul(a, self.inv(b))

    def pow(self, a, b):
        return pow(a % self.p, b, self.p)

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def mat_mul(self, A, B):
        A, B = np.array(A), np.array(B)

        if A.shape[1] != B.shape[0]:
            raise ValueError("A mátrix oszlopainak száma nem egyezik meg B mátrix soraival.")

        result = np.dot(A, B) % self.p
        return result

# Példa használat
if __name__ == "__main__":
    zp = Zp(7)
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print(zp.mat_mul(A, B)) # Matrix multiplication in Z_7
