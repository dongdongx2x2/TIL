import sys
sys.stdin = open('1515_input.txt')

input = sys.stdin.readline

num = input().rstrip()
n = 0
i = 0

while True:
    n += 1

    for c in str(n):
        if num[i] == c:
            i += 1
            if i >= len(num):
                print(n)
                exit()
