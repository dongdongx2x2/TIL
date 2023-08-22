import sys
sys.stdin = open('1120_input.txt')

input = sys.stdin.readline

a, b = input().split()
mxmx = 50

for i in range(len(b)- len(a)+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1

    mxmx = min(mxmx, cnt)
print(mxmx)