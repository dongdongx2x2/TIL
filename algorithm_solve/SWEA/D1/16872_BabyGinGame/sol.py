import sys
sys.stdin = open('16872_input.txt')

T = int(input())

for _ in range(T):

    num = list(map(int, input()))

    v = [0] * 10

    for i in range(6):
        v[num[i]] += 1

    tem = 0
    for i in range(10):

        if v[i] == 3:
            tem += 1
        elif i<8 and (v[i] == 1 and v[i+1] == 1 and v[i+2] == 1):
            tem += 1
            v[i] = 0
            v[i+1] = 0
            v[i+2] = 0

    if tem == 2:
        print(True)
    else:
        print(False)

