import sys
sys.stdin = open('1676_input.txt')

input = sys.stdin.readline

N = int(input())

def fac(N):
    if N == 0:
        return 1

    else:
        return N * fac(N-1)

N = str(fac(N))
N = N[::-1]
cnt = 0
for i in N:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)
