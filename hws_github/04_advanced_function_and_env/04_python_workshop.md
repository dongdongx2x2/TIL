# Workshop

### 1. 간단한 N의 약수 (SWEA #1933)
- 입력으로 1개의 정수 N이 주어진다 . 정수 N의 약수를 오름차순으로 출력하는 프로그램을 작성하시오

```python
# 간단한 N의 약수 

N = int(input()) # 정수 N 받기

num_list = list(range(1,N + 1)) # 리스트 범위 설정

for i in num_list: # 반복하면서
    if N % i == 0: # 나누어 떨어지는 것이 약수
        print(i)
```
### 2. LIst의 합 구하기
- 정수로만 이루어진 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 list_sum 함수를 bilt-in 함수인 sum()함수를 사용하지 않고 작성하시오 .

```python
def list_sum(N):
    result = 0
    for num in N: # 반복문을 통해 하나씩 더하기
        result += num
    return result

print(list_sum([1, 2, 3, 4, 5]))
```
### 3. Dictionary로 이루어진 List의 합 구하기
- Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value 들의 합을 반환하는 dict_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

```python
# Dictionary로 이루어진 List의 합 구하기

def dict_list_sum (dic_list):
    result = 0
    for i in range(len(dic_list)):       
        result += dic_list[i]['age'] # sum() 함수 사용하지 않고 더하기

    return result # 값 반환

print(dict_list_sum([{'name': 'kim', 'age': 12},{'name':'lee', 'age': 4}]))
```

### 4. 2차원 List의 전체 합 구하기
- 정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 all_list_sum 함수를 built-in 함수은 sum() 함수를 사용하지 않고 작성하시오.

```python
def all_list_sum (list):
    list_sum = list[0]+ list[1] +list[2]+list[3]
    result = 0
    for i in list_sum:
        result += i
    return result
print(all_list_sum([[1],[2, 3],[4, 5, 6],[7, 8, 9, 10]]))
```

### 5. 숫자의 의미
- 정수로 이루어진 list를 전달 받아, 정수에 대응되는 아스키 문자를 이어붙인 문자열을 반환하는 get_secret_word 함수를 작성하시오.
```python
def get_secret_word(num_list):
    result = ''
    for i in num_list:
        result += chr(i)
    return result
print(get_secret_word([83, 115, 65, 102, 89]))
```


### 6. 내 이름은 몇일까?
- 문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는 get_secret_numberget_secret_number함수를 작성하시오.단, 문자열은 A~Z, a~z 로만 구성되어 있다.

```python
# 내 이름은 몇일까??

def get_secret_number(str_happy):
    result = 0
    for i in str_happy:
        result += ord(i)
    return result
print(get_secret_number('happy'))
```


### 7. 강한 이름
- 문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하여 더 큰 합을 가진 문자열을 반환하는 get_strong_word함수를 작성하시오. 단, 두 문자열의 아스키 숫자의 합이 같은 경우, 둘 다 반환하세요.

```python
# 강한 이름

def get_secret_number(str_list1, str_list2):
    result1 = 0
    result2 = 0
    for i in str_list1:
        result1 += ord(i)
    for j in str_list2:
        result2 += ord(j)
    if result1 > result2:
        return str_list1
    elif result1 < result2:
        return str_list2
    else: # 값이 같으면 둘다 반환
        return str_list1, str_list2

print(get_secret_number('delilah','dixon'))
```