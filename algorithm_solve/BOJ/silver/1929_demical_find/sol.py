import sys
sys.stdin = open('1929_input.txt')

input = sys.stdin.readline

def demical(n):
    tem = [n]
    for j in range(2, int(i**0.5)+1):
        if n % j == 0:
            return
    print(*tem)

M, N = map(int, input().split())


for i in range(M, N+1):
    if i == 1:
        continue
    else:
        demical(i)