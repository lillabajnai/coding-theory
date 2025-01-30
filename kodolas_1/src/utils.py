# A p,q meghatározása n=pq és \phi(n) ismeretében
def find_p_q(n, phi):
    for p in range(2, n):
        if n % p == 0: # Ha p osztója n-nek, akkor q = n / p
            q = n // p
            if (p - 1) * (q - 1) == phi:
                return p, q
    return None

# A p,q meghatározása n, e és d ismeretében
# φ(n)=(p−1)(q−1)
# e⋅d≡1 (modφ(n))
def find_p_q_given_n_e_d(n, e, d):
    # megfelelő phi(n) meghatározása
    k = d * e - 1

    phi_n = None
    for i in range(2, k + 1):
        if k % i == 0:
            phi_n = k // i
            for p in range(2, int(n ** 0.5) + 1):
                if n % p == 0:  # p egy prímosztója n-nek
                    q = n // p
                    if (p - 1) * (q - 1) == phi_n:
                        return p, q
    return None

if __name__ == "__main__":
    # n = 221  # Ez 13 * 17
    # phi_n = 192  # (13-1) * (17-1) = 192
    #
    # p, q = find_p_q(n, phi_n)
    # print(f"p = {p}, q = {q}")

    n = 3233  # n = p * q
    e = 17
    d = 2753

    result = find_p_q_given_n_e_d(n, e, d)
    if result:
        p, q = result
        print(f"A p és q értékei: p = {p}, q = {q}")
    else:
        print("Nem találhatóak megfelelő p és q értékek.")