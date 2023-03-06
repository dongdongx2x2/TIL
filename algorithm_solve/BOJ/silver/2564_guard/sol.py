import sys
sys.stdin = open('2564_input.txt')

input = sys.stdin.readline

w, h = map(int, input().split()) #w가로, h세로

N = int(input()) # 상점개수

store = [list(map(int, input().split())) for _ in range(N)]
# print(store)
d_dir, d_num = map(int, input().split())
# print(d_dir, d_num)

dir_opposite = [(1, 2), (2, 1), (3, 4), (4, 3)]


result = 0
for i in store: # store 리스트 순회하면서
    if i[0] == d_dir: # 같은 방향에 있다면
        result += abs(i[1] - d_num) # 값을 뺀 절대값
    elif (i[0], d_dir) in dir_opposite: # 반대 방향에 있다면
        if i[0] == 1 or i[0] == 2: # 북남에서 시작
            a = h + i[1] + d_num
            b = h + (w - i[1]) + (w - d_num)
            if a >= b:
                result += b
            else:
                result += a
        else: #동서에서 시작
            a = w + i[1] + d_num
            b = w + (h - i[1]) + (h - d_num)
            if a >= b:
                result += b
            else:
                result += a

    else: # 양옆 방향에 있는경우
        if i[0] == 1: # 상점이가 북에 있고
            if d_dir == 3: #동근이 서
                result += (i[1] + d_num)
            elif d_dir == 4: #동근이 동
                result += ((w-i[1]) + d_num)
        elif i[0] == 2: # 상점이 남
            if d_dir == 3: #동근이 서
                result += (i[1] + (h - d_num))
            elif d_dir == 4: # 동근이 동
                result += ((w-i[1]) + (h - d_num))
        elif i[0] == 3: #상점이 서
            if d_dir == 1: # 동근이 북
                result += (i[1] + d_num)
            elif d_dir == 2: # 동근이 남
                result += ((h-i[1]) + d_num)
        else: # 상점이 동
            if d_dir == 1: # 동근이 북
                result += (i[1] + (w - d_num))
            elif d_dir == 2: # 동근이 남
                result += ((h- i[1]) + (w - d_num))
print(result)