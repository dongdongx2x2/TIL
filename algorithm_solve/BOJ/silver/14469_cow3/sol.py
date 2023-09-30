import sys
sys.stdin = open('14469_input.txt')

input = sys.stdin.readline

N = int(input())

lst = []

for _ in range(N):
    a, b = map(int, input().split())
    lst.append((a,b))
lst.sort(key= lambda x:(x[0]))

ans = 0

for i in range(N):
    if lst[i][0] >= ans:
        ans = lst[i][0] + lst[i][1]

    else:
        ans += lst[i][1]
print(ans)