from sympy import randprime

# (e, n): publikus kulcs
# (d, n): titkos kulcs
def generate_rsa_keys(bits):
    p = randprime(2**(bits-1), 2**bits)
    q = randprime(2**(bits-1), 2**bits)

    # publikus
    n = p * q

    # keressünk 1 < e < phi(n) egészet, hogy lnko(e, phi(n)) = 1
    # titkos
    phi_n = (p - 1) * (q - 1)
    e = 65537  # gyakran használt érték

    # oldjuk meg az ed ≡ 1 (mod phi(n)=(p-1)(q-1)) diofantoszi egyenletet az euklideszi algoritmus segítségével -> d
    d = pow(e, -1, phi_n)
    return (e, n), (d, n)


def rsa_encrypt(message, pubkey):
    e, n = pubkey
    return pow(message, e, n)

def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)


if __name__ == "__main__":
    # RSA kulcsgenerálás
    public_key, private_key = generate_rsa_keys(16)  # Kisebb méretű kulcs a demonstrációhoz
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # Üzenet titkosítása
    message = 42
    ciphertext = rsa_encrypt(message, public_key)
    print("Encrypted:", ciphertext)

    # Üzenet visszafejtése
    decrypted_message = rsa_decrypt(ciphertext, private_key)
    print("Decrypted:", decrypted_message)

    # Ellenőrzés
    assert decrypted_message == message, "Hiba: az RSA dekódolás nem egyezik az eredeti üzenettel!"
