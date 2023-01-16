# workshop

### 1. 문자 print

- `It's SSafy 9`을 출력하는 프로그램을 작성하시오.중간에 작은 따옴표가 있다.)

```python
# 문자열 내부에 작은 따옴표가 있어
# 큰 따옴표로 감싸 주었다.
print("It's SSAFY 9")

# escape sequence를 사용하여
# 작은 따옴표를 작성하였다.
print('It\'s SSAFY 9')
```

### 2. 숫자 print

- `458345 + 623576`를 계산하여 출력하는 프로그램을 작성하시오.

```python
# 더하기
answer = 458345 + 623576
print(answer)
```

### 3. 변수를 사용해서 데이터 출력하기

- 두 변수 greeting, month를 사용해서 `Hello July`를 출력하는 프로그램을 작성하시오.

```python
greeting = 'Hello'
month = 'July'
```

```python
greeting = 'Hello'
month = 'July'
print(greeting, month)
print(f'{greeting} {month}')
```

### 4. 문자형의 입력과 출력

- 입력 받은 문자를 출력하는 프로그램을 작성하시오. (힌트: `input()` 함수를 활용하여 데이터를 입력받을 수 있다.)

```python
hello = input()
```

```markdown
[입력]
문자를 입력받는다.
[출력]
입력 받은 문자를 출력한다.
[입력 예시]
Hello! SSAFY 8
[출력 예시]
Hello! SSAFY 8
```

```python
#hello 변수에 input() 함수의 반환값을 담는다.
#input() 함수는 코드 실행시 사용자가 입력한 값을 그대로 `문자열`로 받아서 반환한다.
    #숫자를 입력하더라도 문자열로 반환한다.
hello = input()

print(hello)
```