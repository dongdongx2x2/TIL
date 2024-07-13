import sys
sys.stdin = open('1114_input.txt')

input = sys.stdin.readline

l, k, c = map(int, input().split())
positions = [0] + list(map(int, input().split())) + [l]
positions = sorted(set(positions))

pieces = [positions[i] - positions[i-1] for i in range(1, len(positions))]

start = 1
end = l

while start <= end:
    mid = (start + end) // 2

    if max(pieces) > mid:
        start = mid + 1

    else:
        total = 0
        cnt = 0

        for p in pieces[::-1]:
            total += p
            if total > mid:
                total = p
                cnt += 1

        if cnt > c:
            start = mid + 1
        else:
            result = mid

            first = total if cnt == c else pieces[0]
            end = mid - 1
print(result, first)