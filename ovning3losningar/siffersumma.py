def siffersum(tal):
    if tal//10==0:
        return tal
    return tal%10 + siffersum(tal//10)

print(siffersum(1997))
