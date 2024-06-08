import sys
sys.stdin = open('15904_input.txt')

input = sys.stdin.readline

import re

if re.match('.*U.*C.*P.*C.*', input()):
    print("I love UCPC")
else:
    print("I hate UCPC")