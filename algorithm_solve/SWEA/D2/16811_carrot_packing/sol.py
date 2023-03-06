import sys
sys.stdin = open('16811_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    minV = 1000
    size = [0] * 31

    for c in lst:
        size[c] += 1

    for i in range(29):     # 1~28 소박스에 들어갈 마지막크기 i
        for j in range(30): # 중박스에 들어갈 마지막크기 j
            A = sum(size[1:i+1])
            B = sum(size[i+1:j+1])
            C = sum(size[j+1:])
            if A*B*C != 0 and A <= N //2 and B <= N //2 and C <= N //2:
                diff = max(A,B,C) - min(A,B,C)
                if minV > diff:
                    minV = diff
    if minV == 1000:
        minV = -1
    print(f'#{tc} {minV}')