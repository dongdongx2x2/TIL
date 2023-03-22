import sys
sys.stdin = open('10808_input.txt')

input = sys.stdin.readline

alphabet = 'abcdefghijklmnopqrstuvwxyz'

word = input().rstrip()

v = [0] * 26

dic = {}

for i in range(26):
    dic[alphabet[i]] = i

for c in word:
    v[dic[c]] += 1
print(*v)