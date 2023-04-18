import sys
sys.stdin = open('1922_input.txt')

input = sys.stdin.readline

def find(x):
    while x != parent[x]:
        x = parent[x]
    return x

N = int(input())
M = int(input())

lst = []

for _ in range(M):
    lst.append(list(map(int,input().split())))

lst.sort(key=lambda x:x[2])

parent = [i for i in range(N+1)]

ans = 0
for s, e, w in lst:
    ss = find(s)
    ee = find(e)

    if ss != ee:
        if ss > ee:
            parent[ss] = ee
        else:
            parent[ee] = ss
        ans += w
print(ans)