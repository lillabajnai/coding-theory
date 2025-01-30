import random

from src.jacobi import jacobi

# k: hány véletlenszerű számot tesztelünk
def solovay_strassen(n, k):
    if n < 2:
        return False
    if n != 2 and n % 2 == 0:
        return False
    for _ in range(k):
        a = random.randint(1, n - 1)
        x = jacobi(a, n)
        # a^(n−1)/2 mod n = x mod n (Euler-féle láncolat)
        if x == 0 or pow(a, (n - 1) // 2, n) != (x % n):
            return False
    return True

if __name__ == "__main__":
    n = 29
    k = 5
    print(f"{n}: {solovay_strassen(n, k)}")  # 29 prím

    n = 30
    k = 5
    print(f"{n}: {solovay_strassen(n, k)}") # False

    n = 97
    k = 5
    print(f"{n}: {solovay_strassen(n, k)}") # True

    n = 100
    k = 5
    print(f"{n}: {solovay_strassen(n, k)}") # False

    n = 91
    k = 5
    print(f"{n}: {solovay_strassen(n, k)}") # False

    n = 2003
    k = 5
    print(f"{n}: {solovay_strassen(n, k)}") # True

    n = 2004
    k = 5
    print(f"{n}: {solovay_strassen(n, k)}") # False