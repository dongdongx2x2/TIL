import sys
sys.stdin = open('14425_input.txt')

input = sys.stdin.readline

N, M = map(int,input().split())
cnt = 0
sett = set()

for _ in range(N):
    a = input().rstrip()
    sett.add(a)

for _ in range(M):
    b = input().rstrip()
    if b in sett:
        cnt += 1

print(cnt)