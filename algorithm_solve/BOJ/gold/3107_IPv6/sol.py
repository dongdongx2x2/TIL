import sys
sys.stdin = open('3107_input.txt')

input = sys.stdin.readline

protocol = input().rstrip()

if "::" in protocol:
    tem = protocol.split("::")
    left = tem[0].split(":") if tem[0] else []
    right = tem[1].split(":") if len(tem) > 1 and tem[1] else []

    missing = 8 - (len(left) + len(right))

    ans = left + ["0000"] * missing + right
else:
    ans = protocol.split(":")

ans = list(map(lambda x: x.zfill(4), ans))
print(':'.join(ans))