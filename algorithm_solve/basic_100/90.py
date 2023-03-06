# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)가
# 공백을 두고 입력된다.(a, m, d는 -50 ~ +50, n은 10이하의 자연수)

a, m, d, n = map(int, input().split())

for _ in range(n-1):
    a *= m
    a += d

print(a)