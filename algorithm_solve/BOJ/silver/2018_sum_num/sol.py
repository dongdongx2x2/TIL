import sys
sys.stdin = open('2018_input.txt')

input = sys.stdin.readline

n = int(input())
cnt, sm = 0, 0
s, e = 0, 0

while e <= n:
    if sm < n:
        e += 1
        sm += e
    elif sm > n:
        sm -= s
        s += 1
    else:
        cnt += 1
        e += 1
        sm += e
print(cnt)
