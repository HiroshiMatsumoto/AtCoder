H, W = map(int, input().split())

start = None
obstacles = []
C = [['' for w in range(W)]for h in range(H)]
for h in range(H):
    line = input().strip()
    for w in range(W):
        C[h][w] = line[w]
        if C[h][w] == 'S':
            start = (h,w)
        elif C[h][w] == '#':
            obstacles.append((h,w))

def search(current, goal, cmap, path):
    H, W = len(cmap), len(cmap[0])
    h, w = current
    start = goal
    reached = False
    path.append(current)
    if 4 <= len(path) and current == goal:
        reached = True
    if not reached and h+1 < H and cmap[h+1][w] != '#' and ((4 <= len(path) and (h+1, w) == start) or ((h+1, w) != start and (h+1, w) not in path)):
        reached = search((h+1, w), goal, cmap, path)
        if len(path) and not reached:
            path.pop()
    if not reached and 0 <= h-1 and cmap[h-1][w] != '#' and ((4 <= len(path) and (h-1, w) == start) or ((h-1, w) != start and (h-1, w) not in path)):
        reached = search((h-1, w), goal, cmap, path)
        if len(path) and not reached:
            path.pop()
    if not reached and w+1 < W and cmap[h][w+1] != '#' and ((4 <= len(path) and (h, w+1) == start) or ((h, w+1) != start and (h, w+1) not in path)):
        reached = search((h, w+1), goal, cmap, path)
        if len(path) and not reached:
            path.pop()
    if not reached and 0 <= w-1 and cmap[h][w-1] != '#' and ((4 <= len(path) and (h, w-1) == start) or ((h, w-1) != start and (h, w-1) not in path)):
        reached = search((h, w-1), goal, cmap, path)
        if len(path) and not reached:
            path.pop()
    return reached

path = []
if search(start, start, cmap=C, path=path):
    print("Yes")
else:
    print("No")
