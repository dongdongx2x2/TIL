import sys
sys.stdin = open('18110_input.txt')

input = sys.stdin.readline

def custom_round(number):
    return int(number + 0.5)

def solve():
    n = int(input())

    if n == 0:
        return 0

    opinions = [int(input()) for _ in range(n)]
    opinions.sort()

    cut = custom_round(n * 0.15)
    trimmed_opinions = opinions[cut:-cut] if cut > 0 else opinions

    average = sum(trimmed_opinions) / len(trimmed_opinions)
    return custom_round(average)

print(solve())