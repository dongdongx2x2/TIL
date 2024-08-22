import sys
sys.stdin = open('28325_input.txt')

input = sys.stdin.readline

n = int(input())
rooms = list(map(int, input().split()))

def solve(arr):
    total = sum(arr)
    if total == 0:
        return n // 2

    idx = 0

    for idx, a in enumerate(arr):
        if a:
            break

    arr = arr[idx + 1:] + arr[:idx + 1]

    v = [0] * n

    for i in range(n):
        if arr[i] or v[i]:
            continue

        for j in range(i, n):
            if arr[j]:
                break

            v[j] = 1
        total += (j-i+1) // 2
    return total

print(solve(rooms))

