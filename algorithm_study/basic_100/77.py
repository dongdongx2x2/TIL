# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합

n = int(input())

s = 0
for i in range(1, n+1):
    if not i % 2:
        s += i

print(s)