import sys
sys.stdin = open('10815_input.txt')

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
M = int(input())
lst2 = list(map(int, input().split()))

dic = {}

for i in lst2:
    dic[i] = 0

for j in lst:
    if j in dic:
        dic[j] = 1

for k in dic:
    print(dic[k], end=' ')


