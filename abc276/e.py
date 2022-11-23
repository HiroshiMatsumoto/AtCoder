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
    # print("IN:", list(map(lambda t:(t[0]+1, t[1]+1), [current])))
    reached = False
    path.append(current)
    if 4 <= len(path) and current == goal:
        print(goal)
        print(path)
        reached = True
        # return reached
    print(current)
    # print(list(map(lambda t:(t[0]+1, t[1]+1), path)))
    if not reached and h+1 < H and cmap[h+1][w] != '#' and (h+1, w) not in path:
        # print("RIGHT:", list(map(lambda t:(t[0]+1, t[1]+1), path)))
        print("RIGHT:", current, " --> ", (h+1, w), end=" || ")
        # print(list(map(lambda t:(t[0]+1, t[1]+1), path)))
        print(path)
        # print((h+1, w), cmap[h+1][w])
        reached = search((h+1, w), goal, cmap, path)
        # print(list(map(lambda t:(t[0]+1, t[1]+1), path)))
        if len(path) and not reached:
            path.pop()
    if not reached and 0 <= h-1 and cmap[h-1][w] != '#' and (h-1, w) not in path:
        # print("LEFT:", list(map(lambda t:(t[0]+1, t[1]+1), path)))
        print("LEFT:", current, " --> ", (h-1, w), end=" || ")
        # print(list(map(lambda t:(t[0]+1, t[1]+1), path)))
        print(path)
        # print((h-1, w), cmap[h-1][w])
        reached = search((h-1, w), goal, cmap, path)
        # print(list(map(lambda t:(t[0]+1, t[1]+1), path)))
        if len(path) and not reached:
            path.pop()
    if not reached and w+1 < W and cmap[h][w+1] != '#' and (h, w+1) not in path:
        # print("DOWN:", list(map(lambda t:(t[0]+1, t[1]+1), path)))
        print("DOWN:", current, " --> ", (h, w+1), end=" || ")
        # print(list(map(lambda t:(t[0]+1, t[1]+1), path)))
        print(path)
        # print((h, w+1), cmap[h][w+1])
        reached = search((h, w+1), goal, cmap, path)
        # print(list(map(lambda t:(t[0]+1, t[1]+1), path)))
        if len(path) and not reached:
            path.pop()
    # (h, w-1) == start(h, w-1) == start or ((h, w-1) != start and (h, w-1) not in path)
    print(current, "UP cond: ", not reached, 0 <= w-1,  cmap[h][w-1] != '#', (h, w-1) == start or ((h, w-1) != start and (h, w-1) not in path))
    if not reached and 0 <= w-1 and cmap[h][w-1] != '#' and ((h, w-1) == start or ((h, w-1) != start and (h, w-1) not in path)):
        # print("UP:", list(map(lambda t:(t[0]+1, t[1]+1), path)))
        print("UP:", current, " --> ", (h, w-1), end=" || ")
        # print(list(map(lambda t:(t[0]+1, t[1]+1), path)))
        print(path)
        # print((h, w-1), cmap[h][w-1])
        reached = search((h, w-1), goal, cmap, path)
        # print(list(map(lambda t:(t[0]+1, t[1]+1), path)))
        if len(path) and not reached:
            path.pop()
    # print(list(map(lambda t:(t[0]+1, t[1]+1), path)))
    """
    if not reached:
        # print(path)
        path.pop()
    """
    # print("OUT:", list(map(lambda t:(t[0]+1, t[1]+1), [current])))
    # print("OUT:", current)
    return reached

        

path = []
# print("start:", start)
print(search(start, start, cmap=C, path=path))
print(list(map(lambda t:(t[0]+1, t[1]+1), path)))
quit()
goaled = False
path = [start]
while not goaled:
    break
    
print(C)

