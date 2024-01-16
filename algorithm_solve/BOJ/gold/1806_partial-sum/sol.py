import sys
sys.stdin = open('1806_input.txt')

input = sys.stdin.readline

n, s = map(int, input().split())
lst = list(map(int, input().split()))

left, right = 0, 0
sm = 0
ans = 1e9

while True:
    if sm >= s:
        ans = min(ans, right - left)
        sm -= lst[left]
        left += 1
    else:
        if right == n:
            break
        sm += lst[right]
        right += 1
if ans == 1e9:
    print(0)
else:
    print(ans)
