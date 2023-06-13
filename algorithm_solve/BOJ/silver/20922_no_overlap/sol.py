import sys
sys.stdin = open('20922_input.txt')

input = sys.stdin.readline
N, K = map(int,input().split())

lst = list(map(int,input().split()))
cnt = [0] * 200001
s = 0
e = 0
ans = 0

while e < N:
    if cnt[lst[e]] < K:
        cnt[lst[e]] += 1
        e += 1
    else:
        cnt[lst[s]] -= 1
        s += 1
    ans = max(ans, e-s)
print(ans)
