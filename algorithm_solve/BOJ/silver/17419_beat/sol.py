import sys
sys.stdin = open('17419_input.txt')

input = sys.stdin.readline

n = int(input())
k = input().strip()

result = k.count('1')

print(result)