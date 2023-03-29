import sys
sys.stdin = open('1920_input.txt')

def binary(n):
    global cnt

    s = 0
    e = len(A)-1

    while s <= e:

        m = (s+e) // 2

        if A[m] == n:
            return 1

        elif A[m] > n:
            e = m - 1
        else:
            s = m + 1
    return 0


input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))


for i in B:
    print(binary(i))


