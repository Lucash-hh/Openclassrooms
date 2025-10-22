def generate_square_dict(n):
    d = dict()
    for i in range(1, n + 1):
        d[i] = i ** 2
    return d

generate_square_dict(8)
print(generate_square_dict(8))