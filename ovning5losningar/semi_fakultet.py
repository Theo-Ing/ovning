def semi_fakultet(n):
    produkt = 1
    for i in range (n, 1, -2):
        produkt *= i
    return produkt

print(semi_fakultet(6))