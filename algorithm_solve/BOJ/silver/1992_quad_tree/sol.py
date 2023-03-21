import sys
sys.stdin = open('1992_input.txt')

input = sys.stdin.readline


N = int(input())

arr = [list(map(int, input().rstrip())) for _ in range(N)]
result = ''
def quad(x, y, K):
    global result

    for i in range(x, x + K):
        for j in range(y, y + K):

            if arr[x][y] != arr[i][j]:

                for a in range(2):
                    for b in range(2):
                        if a == 0 and b == 0:
                            result += '('

                        quad(x + a * K // 2, y + b * K // 2, K // 2)

                        if a == 1 and b == 1:
                            result += ')'


                return

    if arr[x][y] == 0:
        result += '0'
    else:
        result += '1'

quad(0, 0, N)
print(result)