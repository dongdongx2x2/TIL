import sys

sys.stdin = open('2776_input.txt')

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    sset1 = set(map(int, input().split()))
    M = int(input())
    sset2 = list(map(int, input().split()))
    for n in sset2:
        print(1 if n in sset1 else 0)
