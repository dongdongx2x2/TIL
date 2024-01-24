import sys
sys.stdin = open('8983_input.txt')

input = sys.stdin.readline

def hunt(x,y):
    left, right = 0, m-1

    while left <= right:
        mid = (left+right) // 2

        if abs(sade[mid] - x) + y <= l:
            return True

        elif sade[mid] < x:
            left = mid + 1

        else:
            right = mid -1
    return False

m, n, l = map(int, input().split())
sade = list(map(int, input().split()))
animal = [list(map(int, input().split())) for _ in range(n)]

sade.sort()

cnt = 0
for x, y in animal:
    if hunt(x,y):
        cnt += 1
print(cnt)
