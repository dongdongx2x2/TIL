import sys
sys.stdin = open('1978_input.txt')

input = sys.stdin.readline

def demical(n):
    global cnt
    for i in range(2, n):
        if n % i == 0:
            cnt += 1
            return


N = int(input())

lst = list(map(int, input().split()))
cnt = 0

for n in lst:
    if n == 1:
        cnt += 1
    else:
        demical(n)
print(len(lst)-cnt)
