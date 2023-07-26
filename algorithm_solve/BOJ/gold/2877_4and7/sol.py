import sys
sys.stdin = open('2877_input.txt')

input = sys.stdin.readline

K = int(input())

K += 1

a = format(K, 'b')[1:]
a = a.replace('1', '7').replace('0','4')
print(a)