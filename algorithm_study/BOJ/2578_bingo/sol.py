import sys
sys.stdin = open('2578_input.txt')

input = sys.stdin.readline

def check(arr):
    bingo = 0
    for i in arr: # 가로들의 합이 0 이면 원 빙고
        if sum(i) == 0:
            bingo += 1


    for i in range(5): # 세로합 확인
        h = 0
        for j in range(5):
            h += arr[j][i]
        if h == 0:
            bingo += 1


    h = 0
    for i in range(5):
        h += arr[i][i]
    if h == 0:
        bingo += 1

    h = 0
    for i in range(5):
        h += arr[4-i][i]
    if h == 0:
        bingo += 1
    return bingo

def bingogo(bingo):
    k = 0
    while k < 23:
        for i in range(5):
            for j in range(5):
                if bingo[i][j] == num[k]:
                    bingo[i][j] = 0
                    k += 1
                    # print(check(bingo))
                    # print(bingo)
                    if check(bingo) >= 3:
                        return k


bingo = [list(map(int,input().split())) for _ in range(5)]
# num = [list(map(int,input().split())) for _ in range(5)]
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
num3 = list(map(int, input().split()))
num4 = list(map(int, input().split()))
num5 = list(map(int, input().split()))
num = num1 + num2 + num3 + num4 + num5
# print(num)
print(bingogo(bingo))
