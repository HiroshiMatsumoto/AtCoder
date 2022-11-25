N, K = map(int, input().split())
A = input().split()
for i in range(K):
    A.append('0')
print(' '.join(A[K:K+N]))
