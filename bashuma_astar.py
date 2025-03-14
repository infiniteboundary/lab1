import heapq

def f(state):
    goal_pos = {str(i): ((i - 1) // 3, (i - 1) % 3) for i in range(1, 9)}
    goal_pos['x'] = (2, 2) 
    
    res = 0
    for i in range(9):
        if state[i] == 'x':
            continue
        num = state[i]
        cur_x, cur_y = divmod(i, 3)
        goal_x, goal_y = goal_pos[num]
        res += abs(cur_x - goal_x) + abs(cur_y - goal_y) 
    return res

def bfs(start):
    end = "12345678x"
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    operation = ['u', 'r', 'd', 'l']
    
    dist = {}
    prev = {}
    open_list = []
    
    heapq.heappush(open_list, (f(start), start))
    dist[start] = 0
    
    while open_list:
        t = heapq.heappop(open_list)
        state = t[1]
        step = dist[state]
        if state == end:
            break
        x, y = divmod(state.find('x'), 3)
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if 0 <= a < 3 and 0 <= b < 3:
                new_state = list(state)
                new_state[x * 3 + y], new_state[a * 3 + b] = new_state[a * 3 + b], new_state[x * 3 + y]
                new_state = ''.join(new_state)
                if new_state not in dist or dist[new_state] > step + 1:
                    dist[new_state] = step + 1
                    prev[new_state] = (state, operation[i])
                    heapq.heappush(open_list, (dist[new_state] + f(new_state), new_state))
    if end not in prev:
        return "unsolvable"
    result = []
    while end != start:
        result.append(prev[end][1])
        end = prev[end][0]
    result.reverse()
    return ''.join(result)


start_input = input().split()
start = ''.join(start_input)
line = ''.join([c for c in start_input if c != 'x'])
t = 0
for i in range(len(line)):
    for j in range(i + 1, len(line)):
        if line[i] > line[j]:
            t += 1
if t & 1:
    print("unsolvable")
else:
    result = bfs(start)
    print(result)
