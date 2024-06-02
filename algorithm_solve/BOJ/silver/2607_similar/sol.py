import sys
sys.stdin = open('2607_input.txt')

input = sys.stdin.readline

n = int(input())
target = list(input())

ans = 0

for _ in range(n-1):
    compare = target[:]
    word = input()
    cnt = 0

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(compare) < 2:
        ans += 1

print(ans)
