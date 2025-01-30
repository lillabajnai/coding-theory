import random

def miller_rabin(p, num_tests=5):
    # egyszerű esetek
    # ha p 2 vagy 3, akkor prím
    if p == 2 or p == 3:
        return True
    # ha kisebb, mint 2 vagy páros, akkor nem prím.
    if p < 2 or p % 2 == 0:
        return False

    # p-1 = 2^r * m felbontása
    r, m = 0, p-1
    while m % 2 == 0:
        r += 1
        m //= 2

    # ellenőrizzük, hogy a sorozatban megjelenik-e az 1 és előtte -1
    def check(a):
        x = pow(a, m, p)
        if x == 1 or x == p-1:
            return True

        for _ in range(r-1):
            x = pow(x, 2, p)
            if x == p-1:
                return True
            return False # Csak akkor False, ha egyik iterációban sem lett p-1

    for _ in range(num_tests):
        a = random.randint(2, p-2)
        if not check(a):
            return False
        return True

if __name__ == "__main__":
    print(miller_rabin(561))  # False (561 Carmichael-szám)
    print(miller_rabin(37))  # True  (37 prím)
    print(miller_rabin(101))  # True  (101 prím)
    print(miller_rabin(104729))  # True  (104729 prím)
    print(miller_rabin(4))  # False (4 összetett)
