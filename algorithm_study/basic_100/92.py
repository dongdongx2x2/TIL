# 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력

n = int(input())

lst = list(map(int, input().split()))

new_lst = [0]* 23

for i in lst:
    new_lst[i-1] += 1

print(*new_lst)
