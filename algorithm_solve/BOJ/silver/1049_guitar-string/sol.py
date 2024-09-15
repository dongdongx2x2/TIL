import sys
sys.stdin = open('1049_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())

package = []
single = []

for _ in range(m):
    a, b = map(int, input().split())
    package.append(a)
    single.append(b)
    
package = min(package)
single = min(single)

if package < single * 6:
    if package < (n % 6) * single:
        print((n // 6) * package + package)
    else:
        print((n // 6) * package + (n % 6) * single)

elif package >= single * 6:
    print(n * single)
