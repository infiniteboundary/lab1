end = "12345678x"
def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]

def dfs(t, depth, visited, max_depth=33):
    if depth > max_depth:
        return -1
    if t == end:
        return depth
    if t in visited:
        return -1
    visited.add(t) 
    k = t.index('x')
    x, y = k // 3, k % 3
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    min_depth = float('inf') 
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < 3 and 0 <= b < 3:
            arr = list(t)
            swap(arr, k, a * 3 + b)  
            str_state = ''.join(arr)
            res = dfs(str_state, depth + 1, visited, max_depth)
            if res != -1:
                min_depth = min(min_depth, res)  
    visited.remove(t)  
    return min_depth if min_depth != float('inf') else -1  

start = ''.join(input().strip().split())
visited = set() 
print(dfs(start, 0, visited))
