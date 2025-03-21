"""
待补充代码：对搜索过的格子染色
"""
import matplotlib.pyplot as plt
import heapq
from collections import deque
from matplotlib.colors import ListedColormap

def visualize_maze_with_path(maze, path, visited):
    colored_maze = [[0.5 if (i, j) in visited else maze[i][j] for j in range(len(maze[0]))] for i in range(len(maze))]
    colors = ['red', 'blue', 'gray']  
    cmap = ListedColormap(colors)
    plt.figure(figsize=(len(maze[0]), len(maze)))  # 设置图形大小
    plt.imshow(colored_maze, cmap=cmap, vmin=0, vmax=1, interpolation='nearest')  

    # 绘制路径
    if path:
        path_x, path_y = zip(*path)
        plt.plot(path_y, path_x, marker='o', markersize=8, color='red', linewidth=3)

    # 设置坐标轴刻度和边框
    plt.xticks(range(len(maze[0])))
    plt.yticks(range(len(maze)))
    plt.gca().set_xticks([x - 0.5 for x in range(1, len(maze[0]))], minor=True)
    plt.gca().set_yticks([y - 0.5 for y in range(1, len(maze))], minor=True)
    plt.grid(which="minor", color="black", linestyle='-', linewidth=2)

    plt.axis('on')  # 显示坐标轴
    plt.show()

def dfs(maze, x, y, end, path, visited):
    if (x, y) == end:
        path.append((x, y))
        return True
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]) or maze[x][y] == 1 or (x, y) in visited:
        return False
    visited.add((x, y))
    path.append((x, y))
    if dfs(maze, x+1, y, end, path, visited) or dfs(maze, x, y+1, end, path, visited) or dfs(maze, x-1, y, end, path, visited) or dfs(maze, x, y-1, end, path, visited):
        return True
    path.pop()
    return False

def bfs(maze, start, end, path, visited):
    queue = deque([start])
    parent = {start: None}
    visited.add(start)
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append((nx, ny))
                parent[(nx, ny)] = (x, y)
                visited.add((nx, ny))
    if end not in parent:
        return False
    x, y = end
    while (x, y) is not None:
        path.append((x, y))
        next_node = parent[(x, y)] 
        if next_node is None:
            break 
        x, y = next_node
    path.reverse()
    return True


def dijkstra(maze, start, end, path, visited):
    heap = [(0, start)]
    parent = {start: None}
    cost = {start: 0}
    while heap:
        cur_cost, (x, y) = heapq.heappop(heap)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if (x, y) == end:
            while (x, y) is not None:
                path.append((x, y))
                if parent[(x, y)] is None:
                    break
                x, y = parent[(x, y)]
            path.reverse()
            return True
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            new_cost = cur_cost + 1
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                if (nx, ny) not in cost or new_cost < cost[(nx, ny)]:
                    cost[(nx, ny)] = new_cost
                    heapq.heappush(heap, (new_cost, (nx, ny)))
                    parent[(nx, ny)] = (x, y)
    return False


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, end, path, visited):
    heap = [(0, start)]
    parent = {start: None}
    cost = {start: 0}
    while heap:
        _, (x, y) = heapq.heappop(heap)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if (x, y) == end:
            while (x, y) is not None:
                path.append((x, y))
                if parent[(x, y)] is None:
                    break
                x, y = parent[(x, y)]
            path.reverse()
            return True
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            new_cost = cost[(x, y)] + 1
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                if (nx, ny) not in cost or new_cost < cost[(nx, ny)]:
                    cost[(nx, ny)] = new_cost
                    priority = new_cost + heuristic((nx, ny), end)
                    heapq.heappush(heap, (priority, (nx, ny)))
                    parent[(nx, ny)] = (x, y)
    return False

# 提供迷宫的二维数组
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
end = (4, 4)
path = []
visited = set()
algorithm = input("请选择搜索算法 (dfs/bfs/dijkstra/a*): ").strip().lower()
if algorithm == "dfs":
    dfs(maze, start[0], start[1], end, path, visited)
elif algorithm == "bfs":
    bfs(maze, start, end, path, visited)
    print("Visited nodes:", visited)

elif algorithm == "dijkstra":
    dijkstra(maze, start, end, path, visited)
    print("Visited nodes:", visited)

elif algorithm == "a*":
    a_star(maze, start, end, path, visited)
else:
    print("无效的算法选择")

# 假设给定路径的坐标列表
#path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]

# 可视化迷宫及路径
visualize_maze_with_path(maze, path, visited)

