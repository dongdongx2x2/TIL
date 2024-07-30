import sys
sys.stdin = open('20529_input.txt')

input = sys.stdin.readline

def calculate_distance(mbti1, mbti2):
    return sum(1 for a, b in zip(mbti1, mbti2) if a != b)

def min_distance_between_three(students):
    n = len(students)
    if n > 32:
        return 0
    min_distance = float('inf')
    for i in range(n-2):
        for j in range(i + 1, n-1):
            for k in range(j + 1, n):
                dist = (calculate_distance(students[i], students[j]) +
                        calculate_distance(students[j], students[k]) +
                        calculate_distance(students[i], students[k]))
                min_distance = min(min_distance, dist)
    return min_distance

t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(input().split())
    print(min_distance_between_three(lst))