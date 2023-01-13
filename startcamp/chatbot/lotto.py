import random

# 1~45숫자를 담은 list 생성
# range(n,m) = n부터 m-1 까지의 숫자를 생성
numbers = list(range(1, 46))

# numbers가 가진 숫자 중에 무작위 값을 하나씩 6번 뽑기
# 리스트가 가직 있는 값중 무작위 값을 뽑는 법은??
# print(random.choice(numbers))

# while 문을 사용하여 뽑아보기. 

# n = 1

# while n < 7:
#     print(random.choice(numbers))
#     n = n + 1

print(random.sample(numbers,6))