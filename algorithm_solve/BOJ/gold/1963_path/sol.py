import sys
sys.stdin = open('1963_input.txt')

input = sys.stdin.readline
from collections import deque

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def bfs(start, end):
    if start == end:
        return 0

    q = deque()
    q.append((start,0))
    v = set()
    v.add(start)

    while q:
        cur, depth = q.popleft()

        if cur == end:
            return depth

        for neighbor in get_neighbors(cur):
            if neighbor not in v:
                v.add(neighbor)
                q.append((neighbor, depth + 1))

    return "Impossible"

def get_neighbors(prime):
    neighbors = []
    prime_str = str(prime)

    for i in range(4):
        for j in range(10):
            if i == 0 and j == 0:
                continue
            new_prime = int(prime_str[:i] + str(j) + prime_str[i+1:])

            if new_prime in primes:
                neighbors.append(new_prime)
    return neighbors


primes = set()

for i in range(1000, 10000):
    if is_prime(i):
        primes.add(i)

t = int(input())

for _ in range(t):
    start, end = map(int, input().split())
    ans = bfs(start, end)
    print(ans)