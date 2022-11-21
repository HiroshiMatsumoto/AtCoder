N, M = map(int, input().split())

roads = dict()
for i in range(M):
    cityA, cityB = map(int, input().split())
    if cityA not in roads:
        roads[cityA] = list()
    if cityB not in roads:
        roads[cityB] = list()
    roads[cityA].append(cityB)
    roads[cityB].append(cityA)
for city in range(1, N+1):
    if city in roads:
        print(len(roads[city]), " ".join(map(str, sorted(roads[city]))))
    else:
        print(0)
