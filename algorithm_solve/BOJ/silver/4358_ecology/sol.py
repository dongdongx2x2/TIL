import sys
sys.stdin = open('4358_input.txt')

input = sys.stdin.readline

from collections import defaultdict

_dict = defaultdict(int)


cnt = 0
while True:
    a = input().rstrip()
    if not a:
        break
    _dict[a] += 1
    cnt += 1


for key,values in sorted(_dict.items()):
    _dict[key] = values / cnt * 100
    # print("%s %.4f" %(key, _dict[key]))
    print(f"{key} {_dict[key]:.4f}")
