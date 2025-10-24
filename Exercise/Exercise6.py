def create_matrix(M,N):
    matrix = []
    for i in range(M):
        line = []
        for j in range(N):
            line.append(i * j)
        matrix.append(line)
    return matrix

matrix = create_matrix(4,4)
for line in matrix:
    print(' '.join(str(x) for x in line))