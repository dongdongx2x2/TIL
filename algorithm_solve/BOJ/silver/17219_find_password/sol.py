import sys
sys.stdin = open('17219_input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

for _ in range(N):
    a, b = input().split()
    dic[a] = b

for _ in range(M):
    print(dic[input().rstrip()])