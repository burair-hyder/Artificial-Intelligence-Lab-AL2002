# Question 03
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
goal = 'G'


def dls(node, goal, limit, visited, path):
    visited.append(node)
    path.append(node)

    if node == goal:
        return True

    if limit == 0:
        path.pop()
        return False

    for neighbor in graph.get(node, []):
        if neighbor not in path:   
            if dls(neighbor, goal, limit - 1, visited, path):
                return True

    path.pop()
    return False


def ids(start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = []
        path = []

        found = dls(start, goal, depth, visited, path)

        print("Depth Level =", depth)
        print("Visited:", visited)

        if found:
            print("Goal Found!")
            print("Final Path:", path)
            return path

        print("Goal not found at this depth.")
        print("-" * 50)

    print("Goal not found up to max depth =", max_depth)
    return None


# Run IDS (max depth can be set as needed)
ids(start, goal, max_depth=5)
