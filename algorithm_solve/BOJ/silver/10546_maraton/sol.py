import sys
sys.stdin = open('10546_input.txt')

input = sys.stdin.readline


def find_non_finisher():
    n = int(input())

    participants = {}
    for _ in range(n):
        name = input()
        participants[name] = participants.get(name, 0) + 1

    for _ in range(n - 1):
        name = input()
        if name in participants:
            participants[name] -= 1
            if participants[name] == 0:
                del participants[name]

    return list(participants.keys())[0]

print(find_non_finisher())