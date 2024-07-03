import sys
sys.stdin = open('2831_input.txt')

input = sys.stdin.readline

def solve(short, tall):
    global ans

    short_idx = 0
    tall_idx = len(tall) - 1

    while short_idx < len(short) and tall_idx >= 0:
        if short[short_idx] + tall[tall_idx] < 0:
            ans += 1
            short_idx += 1
            tall_idx -= 1
        else:
            tall_idx -= 1

n = int(input())
males = sorted(list(map(int, input().split())))
females = sorted(list(map(int, input().split())))

short_males = []
tall_males = []
short_females = []
tall_females = []

for m in males:
    if m < 0:
        short_males.append(m)
    else:
        tall_males.append(m)

for f in females:
    if f < 0:
        short_females.append(f)
    else:
        tall_females.append(f)

ans = 0

solve(short_males, tall_females)
solve(short_females, tall_males)
print(ans)