import sys
sys.stdin = open('17085_input.txt')

input = sys.stdin.readline

def draw(x, y, size, val):
    for i in range(-size, size + 1):
        arr[x + i][y] = val
        arr[x][y + i] = val

def cal_area(size):
    return 1 + 4 * size

def can_draw(x, y, size):
    if x - size < 0 or x + size >= n or y - size < 0 or y + size >= m:
        return False
    for i in range(-size, size + 1):
        if arr[x + i][y] != "#" or arr[x][y + i] != "#":
            return False
    return True

n, m = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(n)]

# 0, 1, 2, 3, 4, 5, 6, 7 크기까지의 십자가
# 1, 3, 5, 7, 9, 11,13,15 가로 크기
# 1, 5, 9, 13,17,21,25,29 넓이

# 완탑하면서 두개 곱하기 max값 ??
cross = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == "#":
            cross.append((i,j))

ans = 0

for i in range(len(cross)):
    x1, y1 = cross[i]

    for size1 in range(7, -1, -1):

        if not can_draw(x1, y1, size1):
            continue

        draw(x1, y1, size1, ".")
        area1 = cal_area(size1)

        for j in range(i + 1, len(cross)):
            x2, y2 = cross[j]
            for size2 in range(7, -1, -1):

                if not can_draw(x2, y2, size2):
                    continue
                area2 = cal_area(size2)

                ans = max(ans, area1 * area2)
        draw(x1, y1, size1, "#")
print(ans)
