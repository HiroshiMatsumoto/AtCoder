N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(1, M+1):
    B = [j+1 for j in range(N+1)]
    for k in range(1, M+1):
        if i == k:
            continue
        B[A[k-1]-1], B[A[k-1]] = B[A[k]], B[A[k]-1]
    print(i, B)
