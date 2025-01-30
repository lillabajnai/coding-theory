import miller_rabin

p = 561
is_prime = miller_rabin(p, 100)
print(f"Az 561 prím: {is_prime}")