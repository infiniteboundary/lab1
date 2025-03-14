def dijkstra(n, line):
    INF = float('inf')
    dist = [INF] * (n + 1) 
    dist[1] = 0 
    visited = [False] * (n + 1)
    for _ in range(n):
        u = -1
        for i in range(1, n + 1): 
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        if dist[u] == INF: 
            break
        visited[u] = True
        for v, w in line[u]: 
            dist[v] = min(dist[v], dist[u] + w) 

    if dist[n] == INF:
        return -1
    else:
        return dist[n]

n, m = map(int, input().split())
line = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    line[x].append((y, z))
print(dijkstra(n, line))
