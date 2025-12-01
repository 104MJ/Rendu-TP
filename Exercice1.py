def distinct(sequence):
    return len(sequence) == len(set(sequence))

print(distinct([1, 5, 7, 9]))
print(distinct([2, 4, 4, 5, 7, 9]))