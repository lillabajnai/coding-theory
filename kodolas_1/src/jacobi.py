def jacobi(a, n):
    if n <= 0 or n % 2 == 0:
        return 0
    a = a % n
    result = 1
    while a != 0:
        # ha páros
        while a % 2 == 0:
            a //= 2
            if n % 8 in [3, 5]:
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n
    return result if n == 1 else 0

if __name__ == "__main__":
    inputs = [
        (30, 37, "létezik"),
        (10, 17, "nem létezik"),
        (14, 29, "nem létezik"),
        (25, 31, "létezik"),
        (12, 13, "létezik")
    ]

    for a, n, expected in inputs:
        jacobi_value = jacobi(a, n)

        print(f"Teszt: a = {a}, n = {n}, Elvárt eredmény: {expected}")

        if jacobi_value == 1:
            result = "létezik"
        elif jacobi_value == -1:
            result = "nem létezik"
        elif jacobi_value == 0:
            result = "közös osztóik vannak"

        print(f"A {a} négyzetgyöke {result} {n}-nek modulo.")
        print(f"Elvárt: {expected}")
        print()