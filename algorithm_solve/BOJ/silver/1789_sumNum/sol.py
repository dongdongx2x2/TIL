import sys
sys.stdin = open('1789_input.txt')

input = sys.stdin.readline

n = int(input())
i = 0
cnt = 0
while True:
    if n > i:
        i += 1
        n = n - i
        cnt += 1
    else:
        print(cnt)
        break
