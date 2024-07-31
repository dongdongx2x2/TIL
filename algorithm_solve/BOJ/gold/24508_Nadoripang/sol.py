import sys, math
sys.stdin = open('24508_input.txt')

input = sys.stdin.readline

n, k, t = map(int, input().split())
baskets = list(map(int, input().split()))

baskets.sort()  # 바구니를 오름차순으로 정렬

left = 0  # 왼쪽 포인터 (가장 적은 나도리가 있는 바구니)
right = n - 1  # 오른쪽 포인터 (가장 많은 나도리가 있는 바구니)
moves = 0  # 필요한 이동 횟수

while left < right:
    if baskets[right] == k:
        right -= 1
        continue

    if baskets[left] == 0:
        left += 1
        continue

    move = min(k - baskets[right], baskets[left])
    baskets[right] += move
    baskets[left] -= move
    moves += move

    if moves > t:
        print("NO")
        exit()

if sum(baskets) % k == 0:
    print("YES")
else:
    print("NO")