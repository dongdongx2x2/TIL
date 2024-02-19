import sys
sys.stdin = open('18808_input.txt')

input = sys.stdin.readline

def can_stick(x, y, sticker):
    # 스티커 붙일수있는지
    r, c = len(sticker), len(sticker[0])

    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1 and notebook[x+i][y+j] == 1:
                return False
    return True

def stick(x, y, sticker):
    #붙이기
    r, c = len(sticker), len(sticker[0])
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                notebook[x+i][y+j] = 1

def rotate_90(sticker):
    tem = zip(*sticker[::-1])
    return [list(i) for i in tem]

n, m, k = map(int, input().split())

notebook = [[0] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]

    for _ in range(4):
        flag = False
        r, c = len(sticker), len(sticker[0])
        for i in range(n-r+1):
            for j in range(m-c+1):
                if can_stick(i, j, sticker):
                    stick(i, j, sticker)
                    flag = True
                    break

            if flag:
                break
        if flag:
            break
        sticker = rotate_90(sticker)

cnt = 0
for i in range(n):
    for j in range(m):
        if notebook[i][j]:
            cnt += 1
print(cnt)
