from collections import deque

def bfs(start):
    end = "12345678x"
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    distance = 0
    
    while len(queue) > 0:
        for _ in range(len(queue)):
            current_state = queue.popleft()
            if current_state == end:
                return distance
            index_of_x = current_state.index('x')
            x, y = divmod(index_of_x, 3)
            directions_x = [-1, 0, 1, 0]
            directions_y = [0, 1, 0, -1]
            
            for direction in range(4):
                new_x = x + directions_x[direction]
                new_y = y + directions_y[direction]
                if new_x >= 0 and new_x < 3 and new_y >= 0 and new_y < 3:
                    new_state_list = list(current_state)
                    new_index = new_x * 3 + new_y
                    new_state_list[index_of_x], new_state_list[new_index] = new_state_list[new_index], new_state_list[index_of_x]
                    new_state = ''.join(new_state_list)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)
        distance = distance + 1
    return -1

start_input = input().split()
start = ''.join(start_input)
result = bfs(start)
print(result)

