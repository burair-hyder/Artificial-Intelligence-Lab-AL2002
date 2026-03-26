# Task 3: Modified Tree + Minimax + Alpha-Beta Pruning
tree = {
    "Root": ["N1", "N2"],
    "N1": ["N3", "N4"],
    "N2": ["N5", "N6", "N7"],
    "N3": [4, 7],
    "N4": [2, 5],
    "N5": [1, 4],
    "N6": [3, 6],
    "N7": [0, 9]
}


#  MINIMAX 
node_values = {}

def minimax(node, is_max):

    if isinstance(node, int):
        return node

    values = [minimax(c, not is_max) for c in tree[node]]

    best = max(values) if is_max else min(values)
    node_values[node] = best
    return best


# OPTIMAL PATH 
def get_path(node, is_max):
    path = [node]

    if isinstance(node, int):
        return path

    children = tree[node]

    if is_max:
        best = max(children,
                   key=lambda c: c if isinstance(c, int)
                   else node_values[c])
    else:
        best = min(children,
                   key=lambda c: c if isinstance(c, int)
                   else node_values[c])

    return path + get_path(best, not is_max)


#  ALPHA-BETA 
pruned_nodes = []

def collect(node):
    r = [node]
    if not isinstance(node, int):
        for c in tree[node]:
            r.extend(collect(c))
    return r


def alpha_beta(node, alpha, beta, is_max):

    if isinstance(node, int):
        return node

    if is_max:
        value = float("-inf")

        for i, child in enumerate(tree[node]):
            value = max(value,
                        alpha_beta(child, alpha, beta, False))
            alpha = max(alpha, value)

            if alpha >= beta:
                for rem in tree[node][i+1:]:
                    pruned_nodes.extend(collect(rem))  # FIXED
                break

    else:
        value = float("inf")

        for i, child in enumerate(tree[node]):
            value = min(value,
                        alpha_beta(child, alpha, beta, True))
            beta = min(beta, value)

            if alpha >= beta:
                for rem in tree[node][i+1:]:
                    pruned_nodes.extend(collect(rem))  # FIXED
                break

    return value



root_value = minimax("Root", True)
path = get_path("Root", True)

root_ab = alpha_beta("Root",
                     float("-inf"),
                     float("inf"),
                     True)



print("Minimax Root =", root_value)
print("Optimal Path:", " -> ".join(map(str, path)))

print("\nAlpha-Beta Root =", root_ab)
print("Pruned Nodes:", pruned_nodes)


# -------- SHORT COMPARISON --------
# Root value is same for both algorithms (5)
# Alpha-Beta prunes N6 and N7 branches
# Optimal path: Root → N1 → N4 → 5
