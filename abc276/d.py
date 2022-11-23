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
quit()
while True:
    while gc_div < A[idx]:
        if divisible_by(A[idx], 2):
            A[idx] /= 2
            count += 1
        if divisible_by(A[idx], 3):
            A[idx] /= 3
            count += 1
    idx += 1
    if N <= idx:
        break
    print(A)
    """
    if reduce(lambda x,y:x==y,A):
        break
    idx += 1
    if N <= idx:
        break
    if not any(map(lambda x: divisible_by(x,2) or divisible_by(x,3), A)):
        idx += 1
    """
    

while True:
    for x in A:
        print(x, divisible_by(x, 2))
        print(x, divisible_by(x, 3))
    break
    
quit()
divisible_by_or = lambda x: divisible_by_2(x) or divisible_by_3(x)

from functools import reduce
# reduce(lambda x,y: x == y, A)

idx = 0
print(idx, A)
while True:
    # find largest, l, its position l_i, and smallest, m, its position m_i
    m = min(map(lambda x:x if divisible_by_or(x) else None, A))
    l = max(map(lambda x:x if divisible_by_or(x) else None, A))
    # l = max(map(divisible_by_or, A))
    # update A[l_i] = l/m
    A[A.index(l)] = int(l/m)
    print(idx, l, m, A)
    # print(idx, A)
    idx += 1
    if 10 < idx:
        break    
quit()

count = 0
idx = 0
A = sorted(A, reverse=True)
while True:
    print(A)
    x = A[idx]
    if divisible_by_2(x):
        A[idx] = A[idx]/2
        count += 1
    elif divisible_by_3(x):
        A[idx] = A[idx]/3
        count += 1
    if divisible_by_2(x) or divisible_by_3(x):
        continue
    if reduce(lambda x,y: x == y, A):
        break
    idx += 1
    if N <= idx:
        break
if reduce(lambda x,y: x == y, A):
    print(count)
else:
    print(-1)
quit()
while not is_valid and (any(map(lambda x:divisible_by_2(x), A)) or any(map(lambda x:divisible_by_3(x), A))):
    for idx, x in enumerate(A):
        if divisible_by_2(x):
            A[idx] = int(A[idx] / 2)
            count += 1
        if divisible_by_3(x):
            A[idx] = int(A[idx] / 3)
            count += 1
        is_valid = all(map(lambda a:A[0] == a, A))
        if is_valid:
            break

if is_valid:
    print(count)
else:
    print(-1)    
    