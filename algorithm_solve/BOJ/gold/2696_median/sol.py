import sys
sys.stdin = open("2696_input.txt")

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    M = int(input())
    lst = []
    for _ in range(M//10 + 1):
        lst += list(map(int,input().split()))
    # print(lst)

    result = []
    for i in range(0, M, 2):
        tem = sorted(lst[:i+1])
        N = len(tem)
        result.append(tem[N//2])

    n = len(result)
    print(n)
    # print(result)
    for j in range(n//10 + 1):
        print(*result[j*10:j*10+10])

