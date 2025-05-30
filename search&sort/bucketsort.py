def bucketsort(arr):
    buckets = [[] for _ in range(len(arr))]
    for value in arr:
        index = int(value * len(arr))
        buckets[index].append(value)
    return [value for bucket in buckets for value in bucket]

print(bucketsort([0.77, 0.33, 0.44, 0.55, 0.66, 0.77, 0.88, 0.99]))