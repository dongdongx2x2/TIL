import sys
sys.stdin = open('1759_intput.txt')

input = sys.stdin.readline

def dfs(n, s ,tlst):
    if n == L:
        moem = 0
        jaem = 0
        for i in tlst:
            if i in 'aeiou':
                moem += 1
            else:
                jaem += 1
        if moem >= 1 and jaem >= 2:
            ans.append(tlst)
            return

    # cnt = 0
    for j in range(s, C):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, j, tlst + [lst[j]])
            v[j] = 0

L, C = map(int, input().split())

lst = list(input().split())
lst.sort()

v = [0] * C
ans = []
dfs(0,0,[])

for i in ans:
    print(''.join(i))