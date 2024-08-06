import sys

sys.stdin = open('10597_input.txt')

input = sys.stdin.readline


def dfs(depth, arr):
    if depth == len(num):
      print(*arr)
      exit()

    num1 = int(num[depth])
    if not v[num1]:
      v[num1] = 1
      arr.append(num1)
      dfs(depth + 1, arr)
      v[num1] = 0
      arr.pop()
  
    if depth + 1 < len(num):
      num2 = int(num[depth:depth + 2])
      if num2 <= n and not v[num2]:
        v[num2] = 1
        arr.append(num2)
        dfs(depth + 2, arr)
        v[num2] = 0
        arr.pop()
        
num = input().rstrip()
n = len(num) if len(num) < 10 else 9 + (len(num) - 9) // 2
v = [0] * (n + 1)

dfs(0, [])