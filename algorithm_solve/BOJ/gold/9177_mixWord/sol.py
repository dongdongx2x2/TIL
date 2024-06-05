import sys
sys.stdin = open('9177_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(word1, word2, target):
    q = deque([(0,0)])
    v = set((0,0))

    while q:
        i, j = q.popleft()

        if i + j == len(target):
            return True

        if i < len(word1) and word1[i] == target[i + j] and (i+1, j) not in v:
            q.append((i+1, j))
            v.add((i+1, j))

        if j < len(word2) and word2[j] == target[i+j] and (i, j+1) not in v:
            q.append((i, j+1))
            v.add((i, j+1))
    return False



n = int(input())

for i in range(1, n+1):
    word1, word2, target = input().split()

    if bfs(word1, word2, target):
        print(f"Data set {i}: yes")
    else:
        print(f"Data set {i}: no")
