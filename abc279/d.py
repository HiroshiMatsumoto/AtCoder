A, B = map(int, input().split())
g = 1
t = 0

from math import sqrt
res = 0
prev_res = 0
prev_time = -1
count = 0
while True:
    t = count + A/sqrt(g)
    if count != 0 and 0 < t - prev_time:
        break
    prev_time = t
    g += 1
    count += 1
print(prev_time)
