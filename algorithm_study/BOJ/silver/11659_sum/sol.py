import sys
sys.stdin = open('11659_input.txt')

input = sys.stdin.readline

N, M = map(int,input().split())

num = list(map(int, input().split()))

sum_list = [0]
sum = 0
for i in num:
    sum += i
    sum_list.append(sum)
for i in range(M):
    a, b = map(int, input().split())
    print(sum_list[b]-sum_list[a-1])