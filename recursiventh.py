def factorailnth(n):
    if n == 0:
        return 1
    else:
        return n * factorailnth(n-1)

print(factorailnth(5))