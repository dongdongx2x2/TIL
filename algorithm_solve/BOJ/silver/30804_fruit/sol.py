import sys
sys.stdin = open('30804_input.txt')

input = sys.stdin.readline

from collections import defaultdict

n = int(input())
lst = list(map(int, input().split()))

counter = defaultdict(int)
left, right = 0, 0
result = 0

while right < n:
    counter[lst[right]] += 1
    right += 1

    while len(counter) > 2:
        counter[lst[left]] -= 1
        if counter[lst[left]] == 0:
            del counter[lst[left]]
        left += 1

    result = max(result, right - left)

print(result)
