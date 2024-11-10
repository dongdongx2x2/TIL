import sys, heapq
sys.stdin = open('14235_input.txt')

input = sys.stdin.readline

n = int(input())
gifts = []
for _ in range(n):
    visit = list(map(int, input().split()))

    if visit[0] == 0:
        if gifts:
            print(-heapq.heappop(gifts))
        else:
            print(-1)
    else:
        for gift in visit[1:]:
            heapq.heappush(gifts, -gift)