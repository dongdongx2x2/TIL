# 정수 3개를 입력받아 합과 평균을 출력

a, b, c = map(int, input().split())

sum = a + b + c
print(sum, format(sum / 3, '.2f'))