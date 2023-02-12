# 출석을 부른 번호 순서를 바꾸어 공백을 두고 출력

n = int(input())

a = input().split()

for i in range(n-1, -1, -1):
    print(a[i], end = ' ')