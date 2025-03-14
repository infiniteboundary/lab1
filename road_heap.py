class MinHeap:
    def __init__(self):
        self.data = [] 
        self.pos = {} 
    def push(self, d, u):
        self.data.append((d, u))
        self.pos[u] = len(self.data) - 1
        self.up(len(self.data) - 1)
    def pop(self):
        if not self.data:
            return None
        min_item = self.data[0]
        last_item = self.data.pop()
        if self.data:
            self.data[0] = last_item
            self.pos[last_item[1]] = 0
            self.down(0)
        self.pos.pop(min_item[1], None)
        return min_item
    def decrease_key(self, u, new_d):
        if u in self.pos:
            idx = self.pos[u]
            self.data[idx] = (new_d, u)
            self.up(idx)
    def up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] < self.data[parent]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                self.pos[self.data[i][1]], self.pos[self.data[parent][1]] = i, parent
                i = parent
            else:
                break
    def down(self, i):
        size = len(self.data)
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            smallest = i
            if left < size and self.data[left] < self.data[smallest]:
                smallest = left
            if right < size and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest != i:
                self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
                self.pos[self.data[i][1]], self.pos[self.data[smallest][1]] = i, smallest
                i = smallest
            else:
                break
    def empty(self):
        return len(self.data) == 0


def dijkstra(n, line):
    INF = float('inf')
    dist = [INF]*(n+1)
    dist[1] = 0
    pq = MinHeap()
    pq.push(0,1) 
    while not pq.empty():
        d, u = pq.pop()  
        if d > dist[u]:  
            continue
        for v, w in line[u]: 
            if dist[u] + w < dist[v]: 
                dist[v] = dist[u] + w
                pq.push(dist[v], v) 
    return dist[n] if dist[n] != INF else -1

n, m = map(int, input().split())
line = [[] for _ in range(n+1)] 
for _ in range(m):
    x, y, z = map(int, input().split())
    line[x].append((y, z)) 
print(dijkstra(n, line))
