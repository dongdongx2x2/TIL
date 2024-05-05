import sys
sys.stdin = open('15886_input.txt')

input = sys.stdin.readline

n = int(input())
s = input().rstrip()

cnt = 0

for i in range(n-1):
    if s[i:i+2] == "EW":
        cnt += 1
print(cnt)