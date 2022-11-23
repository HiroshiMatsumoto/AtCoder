N = int(input())
A = list(map(int, input().split()))

from math import gcd
g = gcd(*A)

count = 0
is_invalid = False

for idx in range(N):
    A[idx] /= g
    while A[idx]%2 == 0:
        A[idx] /= 2
        count += 1
    while A[idx]%3 == 0:
        A[idx] /= 3
        count += 1
    if A[idx] != 1:
        is_invalid = True
        break
if is_invalid:
    print(-1)
else:
    print(count)
