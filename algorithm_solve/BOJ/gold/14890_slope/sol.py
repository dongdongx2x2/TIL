import sys
sys.stdin = open('14890_input.txt')

input = sys.stdin.readline

def check(lst, v):
    cnt = 1

    for i in range(1, n):
        if lst[i-1] == lst[i]:
            cnt += 1

        elif lst[i-1] + 1 == lst[i] and cnt >= l and v[i-l:i] == [0] * l:
            cnt = 1
            v[i-l:i] = [1] * l
        elif lst[i-1] > lst[i]:
            cnt = 1
        else:
            return False
    return True

n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for _ in range(2):
    for lst in arr:
        v = [0] * (len(lst))

        if check(lst, v) and check(lst[::-1], v[::-1]):
            ans += 1

    arr = list(map(list, zip(*arr)))
print(ans)