import sys
sys.stdin = open('2002_input.txt')

input = sys.stdin.readline

n = int(input())

inner = {input().rstrip(): i for i in range(n)}
outer = [input().rstrip() for i in range(n)]

ans = 0

for i in range(n-1):
    for j in range(i + 1, n):
        if inner[outer[i]] > inner[outer[j]]:
            ans += 1
            break

print(ans)