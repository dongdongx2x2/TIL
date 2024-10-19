import sys
sys.stdin = open('12760_input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())
players = [list(map(int, input().split())) for _ in range(N)]

scores = [0] * N

for _ in range(M):
    max_cards = [max(player) for player in players]

    turn_max = max(max_cards)

    for i in range(N):
        if max_cards[i] == turn_max:
            scores[i] += 1

        players[i].remove(max_cards[i])

max_score = max(scores)

winners = [i + 1 for i, score in enumerate(scores) if score == max_score]

print(*winners)