N = int(input())
S = [input() for _ in range(N)]
FL = 'HDCS'
SL = 'A23456789TJQK'
if all(map(lambda txt:txt[0] in FL and txt[1] in SL, S)) and len(S) == len(set(S)):
    print('Yes')
else:
    print('No')



