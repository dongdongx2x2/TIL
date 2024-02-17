import sys, math
sys.stdin = open('9613_input.txt')

input = sys.stdin.readline

n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))

    sm = 0
    for j in range(1, len(arr)):
        for k in range(j+1, len(arr)):
            sm += math.gcd(arr[j], arr[k])
    print(sm)