# Task 2
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
pruned_nodes = []
node_values = []

def alpha_beta(node, depth, alpha, beta, is_max):
    visited_order.append(node)

    # Leaf node
    if isinstance(node, int):
        return node

    if is_max:
        value = float('-inf')

        for i, child in enumerate(tree[node]):
            child_value = alpha_beta(child, depth + 1, alpha, beta, False)
            value = max(value, child_value)
            alpha = max(alpha, value)

            print(f"Visited {child} from {node} | alpha = {alpha}, beta = {beta}")

            if alpha >= beta:
                # remaining children pruned
                for remaining_child in tree[node][i+1:]:
                    pruned_nodes.append(remaining_child)
                break

    else:
        value = float('inf')

        for i, child in enumerate(tree[node]):
            child_value = alpha_beta(child, depth + 1, alpha, beta, True)
            value = min(value, child_value)
            beta = min(beta, value)

            print(f"Visited {child} from {node} | alpha = {alpha}, beta = {beta}")

            if alpha >= beta:
                # remaining children pruned
                for remaining_child in tree[node][i+1:]:
                    pruned_nodes.append(remaining_child)
                break

    node_values.append((node, value))
    return value

result = alpha_beta("Root", 0, float('-inf'), float('inf'), True)

print("\nVisited Order:")
print(visited_order)

print("\nMinimax Values:")
for node, value in node_values:
    print(f"{node} = {value}")

print("\nPruned Nodes:")
if pruned_nodes:
    print(pruned_nodes)
else:
    print("None")

print(f"\nOptimal value at Root = {result}")
