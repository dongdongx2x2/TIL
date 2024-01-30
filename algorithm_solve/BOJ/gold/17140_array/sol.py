import sys
sys.stdin = open('17140_input.txt')

input = sys.stdin.readline

from collections import Counter

r, c, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(3)]

r, c = r - 1, c - 1

def operate(arr):
    max_len = 0
    new_arr = []
    for row in arr:
        cnt_row = Counter(row)
        if cnt_row.get(0):
            del cnt_row[0]
        sorted_row = sorted(cnt_row.items(), key=lambda x: (x[1], x[0]))
        new_row = []

        for num, freq in sorted_row:
            new_row.append(num)
            new_row.append(freq)
        max_len = max(max_len, len(new_row))
        new_arr.append(new_row)

    for i in range(len(new_arr)):
        if len(new_arr[i]) < max_len:
            new_arr[i] += [0] * (max_len - len(new_arr[i]))
        new_arr[i] = new_arr[i][:100]
    return new_arr


time = 0
while time <= 100:
    if r < len(arr) and c < len(arr[0]) and arr[r][c] == k:
        print(time)
        break
    if len(arr) >= len(arr[0]):
        arr = operate(arr)
    else:
        arr = list(map(list, zip(*arr)))
        arr = operate(arr)
        arr = list(map(list, zip(*arr)))
    time += 1
else:
    print(-1)