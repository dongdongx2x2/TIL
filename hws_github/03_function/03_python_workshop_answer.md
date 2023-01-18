# WorkShop

### 세로로 출력하기

- 자연수 number를 입력 받아, 1부터 number까지의 수를 세로로 한줄씩 출력하시오.

```python
# 세로로 출력하기
number = int(input())

# 1부터 10까지의 숫자를 만들어야 한다.
# range(start, end, step) -> start 부터 end-1 까지 step단계로 정수 범위 만들어줌
range_number = range(1, number + 1)

for num in range_number: # 1, 2, 3, 4, 5 ... -> num 변수에 순서대로
    print(num)
```
  
  

### 가로로 출력하기

* 자연수 number를 입력 받아, 1부터 number까지의 수를 가로로 한칸씩 띄어 출력하시오.

```python
# 가로로 출력하기
number = int(input())
for num in range(1, number + 1):
    print(num, end = ' ') ## built in function, print함수의 디폴트값 바꾸기
```
  
  

### 거꾸로 세로로 출력하기

- 자연수 number를 입력 받아, number부터 0까지의 수를 세로로 한줄씩 출력하시오.
```python
# 거꾸로 세로로 출력하기
number = int(input())
for num in range(number, -1, -1): # ramge (start, end, step =1) 시작 끝 단계 
    print(num)

```
  

### 거꾸로 출력해 보아요 (SWEA #1545)

* 자연수 number를 입력 받아, number부터 0까지의 수를 가로로 한칸씩 띄어 출력하시오.

```python
# 거꾸로 가로로 출력하기 (swea #1545)

number = int(input())

for num in range(number, -1, -1):
    print(num, end = ' ')
```

  

### N줄 덧셈 (SWEA #2025)

- 입력으로 자연수 number가 주어질 때, 1부터 주어진 자연수 number까지를 모두 더한
  값을 출력하시오. 단, 주어지는 숫자는 10000을 넘지 않는다. 예를 들어, 주어진 숫자가
  10일 경우 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55이므로, 출력해야 할 값은 55이다.
  
```python
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
```
  

### 삼각형 출력하기

* 자연수 number를 입력 받아, 아래와 같이 높이가 number인 삼각형을 출력하시오.
```markdown
[입력 예시 ]
7
[출력 예시 ]
      *
     **
    ***
   ****
  *****
 ******
*******

```

```python
# 반복문 두번 써서 만들기
number = int(input())
for star in range(1, number + 1):
    for space in range(number - star-1, -1, -1):
        print(' ', end ='')
    print('*' * star)
```
  

### 중간값 찾기 (SWEA #2063 변형)

- 중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를
  뜻한다. 리스트 numbers에 입력된 숫자에서 중간값을 출력하라.
  
  ```python
  numbers = [
  85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
  51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
  52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24,
  ]
  ```


### 반복문 두번 연습용 

```python
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
```