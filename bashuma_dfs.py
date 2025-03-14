def swap_elements(state, idx1, idx2):
    new_state = state[:]
    new_state[idx1], new_state[idx2] = new_state[idx2], new_state[idx1]
    return new_state

def neighbor_state(state):
    neighbours = []
    idx = state.index('x')
    x, y = divmod(idx, 3)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_idx = new_x * 3 + new_y
            new_state = state[:]
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbours.append(new_state)
    return neighbours


def depth_first_search(state, visited, remaining_depth):
    goal = ['1', '2', '3', '4', '5', '6', '7', '8', 'x']
    if remaining_depth <= 0:
        return False
    if (state == goal):
        return True
    visited.add(tuple(state))
    for neighbour in neighbor_state(state):
        if tuple(neighbour) not in visited:
            if depth_first_search(neighbour, visited, remaining_depth - 1):
                return True
    return False

input_list = input().strip().split()
initial_state = input_list[:]

limit = 33 #查阅资料可知八数码最多31步可以解决
visited_states = set()
if depth_first_search(initial_state, visited_states, limit):
    print(1)
else:
    print(0)
