import heapq

def dijkstra(start):
    end = "12345678x"
    pq = [] 
    heapq.heappush(pq, (0, start))
    visited = {} 
    visited[start] = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] 
    while pq:
        distance, current_state = heapq.heappop(pq)
        if current_state == end:
            return distance
        index_of_x = current_state.index('x')
        x, y = divmod(index_of_x, 3)
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state_list = list(current_state)
                new_index = new_x * 3 + new_y
                new_state_list[index_of_x], new_state_list[new_index] = new_state_list[new_index], new_state_list[index_of_x]
                new_state = ''.join(new_state_list)
                new_distance = distance + 1
                if new_state not in visited or new_distance < visited[new_state]:
                    visited[new_state] = new_distance
                    heapq.heappush(pq, (new_distance, new_state))


start_input = input().split()
start = ''.join(start_input)
result = dijkstra(start)
print(result)
