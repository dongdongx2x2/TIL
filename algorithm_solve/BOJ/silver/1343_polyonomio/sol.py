import sys

sys.stdin = open('1343_input.txt')

input = sys.stdin.readline

board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)

else:
    print(board)
