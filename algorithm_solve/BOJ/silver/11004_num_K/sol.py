import sys
sys.stdin = open('11004_input.txt')

input = sys.stdin.readline

N, K = map(int, input().split())

lst = list(map(int, input().split()))

lst.sort()

print(lst[K-1])