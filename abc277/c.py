N = int(input())
from collections import defaultdict
AtoB = defaultdict(list)

start = 1

for _ in range(N):
    A, B = map(int, input().strip().split())
    AtoB[A].append(B)
    AtoB[B].append(A)

path = set()
floor = start
while floor in AtoB:
    next_floor = max(AtoB[floor])
    if next_floor < floor or next_floor in path:
        break
    path.add(next_floor)
    floor = next_floor
print(floor)    

