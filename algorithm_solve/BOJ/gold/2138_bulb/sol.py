import sys
sys.stdin = open('2138_input.txt')

input = sys.stdin.readline

def change(A, B):
    A1 = A[:]
    cnt = 0
    for i in range(1, n):
        if A1[i-1] == B[i-1]:
            continue

        cnt += 1
        for j in range(i-1, i+2):
            if j < n:
                A1[j] = 1 - A1[j]

    if A1 == B:
        return cnt
    else:
        return 1e9

n = int(input())
lst = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))

tem = change(lst, target)

lst[0] = 1 - lst[0]
lst[1] = 1 - lst[1]

tem = min(tem, change(lst, target) + 1)

if tem != 1e9:
    print(tem)
else:
    print(-1)




