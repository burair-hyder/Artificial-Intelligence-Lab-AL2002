# Question 01:
building = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1]
]

start = (0, 0)
goal  = (3, 3)

R = len(building)
C = len(building[0])

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

adj = {}
for r in range(R):
    for c in range(C):
        if building[r][c] == 1:
            node = (r, c)
            adj[node] = []
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and building[nr][nc] == 1:
                    adj[node].append((nr, nc))


queue = [start]
front = 0  # queue pointer
visited = set([start])
parent = {start: None}
traversal = []

while front < len(queue):
    u = queue[front]
    front += 1

    traversal.append(u)

    if u == goal:
        break

    for v in adj.get(u, []):
        if v not in visited:
            visited.add(v)
            parent[v] = u
            queue.append(v)


path = []
if goal in parent:
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

print("Adjacency List:")
for k in adj:
    print(k, "->", adj[k])

print("\nTraversal order:", traversal)
print("Shortest path:", path)
print("Shortest distance (moves):", len(path) - 1 if path else "No path")
