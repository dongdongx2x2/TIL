# 1, 2, 3, 4, 5 ... 순서대로 계속 더해가다가, 그 합이 입력된 정수보다 커지거나 같아지는 경우,
# 그때까지의 합을 출력

n = int(input())

s = 0
for i in range(1, n+1):
    s += i 
    if s >= n:
        print(s)
        break