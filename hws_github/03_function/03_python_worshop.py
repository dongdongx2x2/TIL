# 세로로 출력하기
number = int(input())

# 1부터 10까지의 숫자를 만들어야 한다.
# range(start, end, step) -> start 부터 end-1 까지 step단계로 정수 범위 만들어줌
range_number = range(1, number + 1)

for num in range_number: # 1, 2, 3, 4, 5 ... -> num 변수에 순서대로
    print(num)


# 가로로 출력하기
number = int(input())
for num in range(1, number + 1):
    print(num, end = ' ') ## built in function, print함수의 디폴트값 바꾸기


# 거꾸로 세로로 출력하기
number = int(input())
for num in range(number, -1, -1): # ramge (start, end, step =1) 시작 끝 단계 
    print(num)


# 거꾸로 가로로 출력하기 (swea #1545)

number = int(input())

for num in range(number, -1, -1):
    print(num, end = ' ')


# N줄 덧셈 (SWEA # 2025)
number = int(input())
result = 0
for num in range(1, number + 1):
    result += num
    # 0 += 1
    # 1 += 2
    # 3 += 3
    # 6 += 4
print(result)


# 삼각형 출력하기
# 문장열의 특성 이용하기
number = int(input())
for num in range(1, number + 1):
    # 문자열 *을 출력할건데
    #문자열은 곱셉이 가능함.
    # 빈 문자열 말고 ' ' 공백도 문자열이다.
    print(' ' * (number - num), '*' * num)
    

# 반복문 두번 써서 만들기
number = int(input())
for star in range(1, number + 1):
    for space in range(number - star-1, -1, -1):
        print(' ', end ='')
    print('*' * star)



# 추가 퀴즈
# 반복문 두번 한거 연습용!!


arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(arr)

for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j])


