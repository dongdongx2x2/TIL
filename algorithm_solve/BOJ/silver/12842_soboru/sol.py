import sys
sys.stdin = open('12842_input.txt')

input = sys.stdin.readline

n, s = map(int, input().split())
m = int(input())
time = [int(input()) for _ in range(m)]

t = 0

while n != s:
    for i in range(m):
        if t % time[i] == 0:
            n -= 1
            if n == s:
                print(i + 1)
                break
    t += 1