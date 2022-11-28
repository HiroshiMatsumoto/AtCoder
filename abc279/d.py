A, B = map(int, input().split())
import math
x = (math.pow(2*B/A, -2/3) - 1)
print(A/math.sqrt(x + 1) + B*x)