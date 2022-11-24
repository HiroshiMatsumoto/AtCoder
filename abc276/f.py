N = int(input())
A = list(map(int, input().split()))

import itertools as itr
from collections import Counter
from math import gcd

for k in range(N):
    if k != 1:
        continue
    num = sum(max(comb) * num for comb, num in Counter(itr.product(A[:k+1], A[:k+1])).items())
    den = sum(Counter(itr.product(A[:k+1], A[:k+1])).values())
    g = gcd(num, den)
    while g != 1:
        num = int(num/g)
        den = int(den/g)
        g = gcd(num, den)
    R = 0
    for i in range(998244353):  
        if (i * den) % 998244353 == num:
            R = i
            break
    print(R)


