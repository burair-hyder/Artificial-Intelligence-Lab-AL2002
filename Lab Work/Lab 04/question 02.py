# Question 02

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': []
}
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': []
}

start = 'A'
goal = 'H'


def dls(node, goal, limit, visited, path):
  
    visited.append(node)
    path.append(node)

    # goal test
    if node == goal:
        return True

    
    if limit == 0:
        path.pop()
        return False

  
    for neighbor in graph.get(node, []):
       
        if neighbor not in path:
            found = dls(neighbor, goal, limit - 1, visited, path)
            if found:
                return True

  
    path.pop()
    return False


def run_dls(depth_limit):
    visited = []
    path = []
    found = dls(start, goal, depth_limit, visited, path)

    print("Depth Limit =", depth_limit)
    print("Visited:", visited)

    if found:
        print("Path Found:", path)
    else:
        print("Path Found: None (Goal not reachable within depth limit)")
    print("-" * 50)



run_dls(2)
run_dls(3)
