import sys
sys.stdin = open('5800_input.txt')

input = sys.stdin.readline


def process_class(scores):
    scores.sort(reverse=True)
    max_score = scores[0]
    min_score = scores[-1]

    largest_gap = max(scores[i] - scores[i + 1] for i in range(len(scores) - 1))

    return max_score, min_score, largest_gap

K = int(input())

for class_num in range(1, K + 1):
    data = list(map(int, input().split()))
    N = data[0]  # 학생 수
    scores = data[1:]  # 점수들

    max_score, min_score, largest_gap = process_class(scores)

    print(f"Class {class_num}")
    print(f"Max {max_score}, Min {min_score}, Largest gap {largest_gap}")
