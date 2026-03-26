# Task 1
tree = {
    "Root": ["N1", "N2"],
    "N1": ["N3", "N4"],
    "N2": ["N5", "N6"],
    "N3": [4, 7],
    "N4": [2, 5],
    "N5": [1, 8],
    "N6": [3, 6]
}

visited_order = []
node_values = {}

def minimax(node, is_max):
    visited_order.append(node)

    
    if isinstance(node, int):
        return node

    children = tree[node]
    values = []

    for child in children:
        value = minimax(child, not is_max)
        values.append(value)

    if is_max:
        best = max(values)
    else:
        best = min(values)

    node_values[node] = best
    return best

# Run Minimax
result = minimax("Root", True)

print("Visited Order:")
print(visited_order)

print("\nMinimax Values:")
for node, value in node_values.items():
    print(f"{node} = {value}")


print(f"\nOptimal value at Root = {result}")
