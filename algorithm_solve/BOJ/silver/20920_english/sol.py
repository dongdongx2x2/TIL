import sys
sys.stdin = open('20920_input.txt')

input = sys.stdin.readline

from collections import defaultdict

n, m = map(int, input().split())
words = [input().rstrip() for _ in range(n)]

word_cnt = defaultdict(int)

for word in words:
    if len(word) >= m:
        word_cnt[word] += 1

sorted_words = sorted(word_cnt.keys(), key=lambda x: (-word_cnt[x], -len(x), x))
for word in sorted_words:
    print(word)