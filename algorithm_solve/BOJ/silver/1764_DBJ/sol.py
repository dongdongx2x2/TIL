import sys
sys.stdin = open('1764_input.txt')

input = sys.stdin.readline

N, M = map(int,input().split())

a = set()
for _ in range(N):
    tem = input().rstrip()
    a.add(tem)

b = set()
for _ in range(M):
    tem = input().rstrip()
    b.add(tem)

ans = sorted(list(a & b))
print(len(ans))
for i in ans:
    print(i)