# Question 04:
graph = {
    'S': {'A': 4, 'B': 2},
    'A': {'C': 5, 'D': 10},
    'B': {'E': 3},
    'C': {'G': 4},
    'D': {'G': 1},
    'E': {'D': 4},
    'G': {}
}

start = 'S'
goal = 'G'


def ucs(graph, start, goal):
    
    frontier = [[0, start]]
    parent = {start: None}
    best_cost = {start: 0}
    visited_order = []

    while len(frontier) > 0:
        
        min_index = 0
        for i in range(1, len(frontier)):
            if frontier[i][0] < frontier[min_index][0]:
                min_index = i

        cost, node = frontier.pop(min_index)
        visited_order.append((node, cost))

        
        if cost != best_cost.get(node, float('inf')):
            continue

      
        if node == goal:
            
            path = []
            cur = goal
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            return path, cost, visited_order

    
        for nbr in graph.get(node, {}):
            edge_cost = graph[node][nbr]
            new_cost = cost + edge_cost

            if nbr not in best_cost or new_cost < best_cost[nbr]:
                best_cost[nbr] = new_cost
                parent[nbr] = node
                frontier.append([new_cost, nbr])

    return None, None, visited_order


path, total_cost, visited = ucs(graph, start, goal)

print("Visited order (node, cost_when_popped):", visited)

if path is not None:
    print("Least cost path:", " -> ".join(path))
    print("Total cost:", total_cost)
else:
    print("No path found.")
