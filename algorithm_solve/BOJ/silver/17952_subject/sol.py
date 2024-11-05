import sys
sys.stdin = open('17952_input.txt')

input = sys.stdin.readline

N = int(input())
stack = []
total_score = 0
current_task = None

for _ in range(N):
    task = input().split()

    if task[0] == '1':
        A, T = int(task[1]), int(task[2])
        if current_task:
            stack.append(current_task)
        current_task = [A, T]

    if current_task:
        current_task[1] -= 1
        if current_task[1] == 0:
            total_score += current_task[0]
            if stack:
                current_task = stack.pop()
            else:
                current_task = None

print(total_score)