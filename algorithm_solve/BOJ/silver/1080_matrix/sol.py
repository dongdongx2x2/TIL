import sys
sys.stdin = open('1080_input.txt')

input = sys.stdin.readline

def flip(A, i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            A[x][y] = 1 - A[x][y]

def solution(N, M, A, B):
    count = 0
    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] != B[i][j]:
                flip(A, i, j)
                count += 1

    return count if A == B else -1


N, M = map(int, input().split())
A = [list(map(int, list(input().rstrip()))) for _ in range(N)]
B = [list(map(int, list(input().rstrip()))) for _ in range(N)]

print(solution(N, M, A, B))