H, W = map(int, input().strip().split())
S = [input().strip() for _ in range(H)]
T = [input().strip() for _ in range(H)]

matched = False
if tuple(S) == tuple(T):
    print('Yes')
    matched = True
if not matched:
    from itertools import permutations as perm
    for p in perm(range(W)):
        txtS = "".join(''.join(S[h][w] for w in p) for h in range(H))
        if txtS == ''.join(T):
            matched = True
            break
    if matched:
        print("Yes")
    else:
        print("No")
