import sys
sys.stdin = open('1269_input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())
a = set(map(int,input().split()))
b = set(map(int,input().split()))

print(len(a-b)+len(b-a))