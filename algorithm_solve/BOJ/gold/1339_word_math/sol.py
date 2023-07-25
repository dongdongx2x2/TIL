import sys
sys.stdin = open('1339_input.txt')

input = sys.stdin.readline
from collections import defaultdict

N = int(input())

words = []
for _ in range(N):
    a = input().rstrip()
    words.append(a)


dic = defaultdict(int)
for word in words:
    for idx, char in enumerate(word):
        # print(len(word)-idx-1, char)
        tem = len(word)-idx-1
        dic[char] += 10 ** tem

values = sorted(dic.values(), reverse=True)

ans = 0
for idx, value in enumerate(values):
    ans += value * (9-idx)
print(ans)