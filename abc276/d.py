N = int(input())
A = list(map(int, input().split()))

divisible_by_2 = lambda a:2 <= a and a%2 == 0
divisible_by_3 = lambda a:3 <= a and a%3 == 0

count = 0
while any(map(lambda x:divisible_by_2(x), A)) or any(map(lambda x:divisible_by_3(x), A)):
    for idx, x in enumerate(A):
        if divisible_by_2(x):
            A[idx] = int(A[idx] / 2)
            count += 1
        if divisible_by_3(x):
            A[idx] = int(A[idx] / 3)
            count += 1

from functools import reduce

if reduce(lambda x,y: x == y, A):
    print(count)
else:
    print(-1)    