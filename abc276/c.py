N = int(input())
P = list(map(int, input().split()))
# 右端から最大値検索
i = N - 2
while P[i] < P[i+1]:
    i -= 1
# 右端からiの範囲で最大値検索
j = N - 1
while P[i] < P[j]:
    j -= 1
# i,j位置の値をswap
P[i], P[j] = P[j], P[i]

print(" ".join(map(str,P[:i + 1] + P[:i:-1])))
