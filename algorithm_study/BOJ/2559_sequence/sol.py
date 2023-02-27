import sys
sys.stdin = open('2559_input.txt')

input = sys.stdin.readline

N, K = map(int, input().split())

data = list(map(int, input().split()))


a = sum(data[:K])
result = [a]
# print(a)
for i in range(N-K):
    result.append(result[-1]-data[i]+data[i+K])
print(max(result))


