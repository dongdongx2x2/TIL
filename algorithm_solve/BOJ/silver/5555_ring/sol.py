import sys
sys.stdin = open('5555_input.txt')

input = sys.stdin.readline

word = input().rstrip()
N = int(input())
cnt = 0

for _ in range(N):
    a = input().rstrip()
    if word in a*2:
        cnt += 1
print(cnt)
