import sys
sys.stdin = open('2023_input.txt')

input = sys.stdin.readline

def prime(x):

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def dfs(depth, st):

    if not prime(int(st)):
        return

    if depth == N:
        result.append(st)
        return

    for k in PN1:
        dfs(depth + 1, st + k)




N = int(input())

## 소수 2,3,5,7 하지만 뒤에 숫자는 1이 붙ㅇ어도된다.

result = []

PN = '2357'
PN1 = '13579'

for i in PN:
    dfs(1, i)

for n in sorted(result):
    print(n)

