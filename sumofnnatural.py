def sum_n_natural(n):
    if n <= 0:
        return 0
    return n+sum_n_natural(n-1)
print(sum_n_natural(5))