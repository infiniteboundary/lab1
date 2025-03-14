from collections import deque

def bfs(n, line):
    queue = deque([1])
    dist = [-1] * (n + 1) 
    dist[1] = 0 

    while queue:
        u = queue.popleft()
        for v in line[u]: 
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)

    return dist[n] 


n, m = map(int, input().split())
line = [[] for _ in range(n + 1)] 
for _ in range(m):
    a, b = map(int, input().split())
    line[a].append(b) 
print(bfs(n, line))
