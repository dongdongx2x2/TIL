import sys
sys.stdin = open('17829_input.txt')

input = sys.stdin.readline

def pool_222(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]

    new_matrix = []
    for i in range(0, n, 2):
        row = []
        for j in range(0, n, 2):
            square = [
                matrix[i][j], matrix[i][j + 1],
                matrix[i + 1][j], matrix[i + 1][j + 1]
            ]
            row.append(sorted(square)[-2])
        new_matrix.append(row)

    return pool_222(new_matrix)

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

result = pool_222(matrix)
print(result)