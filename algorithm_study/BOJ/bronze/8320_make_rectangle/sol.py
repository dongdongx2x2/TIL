import sys
sys.stdin = open('8320_input.txt')

input = sys.stdin.readline

n = int(input())

#1,1 1,2 1,3 1,4 1,5 1,6
#2,1 2,2 2,3
#3,1 3,2

# 곱해서 6 이하의 수 순열 구하기...?
if n == 1:
    print(1)
else:
    cnt = 0
    for i in range(1, n):
        for j in range(i, n+1):
            if i*j <= n:
                cnt += 1
    print(cnt)
