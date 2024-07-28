import sys
sys.stdin = open('20004_input.txt')

input = sys.stdin.readline

a = int(input())

for i in range(1, a + 1):
    tem = i + 1

    if 30 % tem == 0:
        print(i)