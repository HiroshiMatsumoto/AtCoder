H, W = map(int, input().strip().split())
S = [input().strip() for _ in range(H)]
T = [input().strip() for _ in range(H)]

def transpose(S):
    return list(zip(*S[:H]))

S = sorted(transpose(S))
T = sorted(transpose(T))

valid = True
for s, t in zip(S, T):
    if s != t:
        valid = False
        break
if valid:
    print('Yes')
else:
    print('No')
