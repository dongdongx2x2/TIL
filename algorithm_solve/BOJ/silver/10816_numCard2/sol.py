import sys
sys.stdin = open('10816_input.txt')

input = sys.stdin.readline

n = int(input())
lst_n = list(map(int, input().split()))
m = int(input())
lst_m = list(map(int, input().split()))

dic = {}

for i in lst_n:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in lst_m:
    if i in dic:
        print(dic[i], end= " ")
    else:
        print(0, end=" ")