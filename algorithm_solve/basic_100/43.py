# 실수 2개(f1, f2)를 입력받아
# f1 을 f2 로 나눈 값을 출력

f1, f2 = map(float, input().split())

c = f1 / f2
print(format(c, '.3f'))