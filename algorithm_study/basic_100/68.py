# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력
n = int(input())

if n >= 90:
    print('A')
elif 90 > n >= 70:
    print('B')
elif 70 > n >= 40:
    print('C')
else:
    print('D')
