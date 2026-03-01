# Question 05:

GRAPH = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'D': [], 'E': [], 'F': [], 'G': [],
    'J': [], 'K': [], 'L': [], 'M': []
}

START = 'S'
GOALS = ['D', 'E', 'F', 'G', 'J', 'K', 'L', 'M']


class MazeEnvironment:
    def __init__(self, graph, start, goals, undirected=True):
        self.start = start
        self.goals = goals[:]
        self.goal_index = {g: i for i, g in enumerate(goals)}
        self.ALL_MASK = (1 << len(goals)) - 1
        self.graph = self._make_undirected(graph) if undirected else graph

    def _make_undirected(self, g):
        newg = {}
        for u in g:
            newg[u] = []
        for u in g:
            for v, w in g[u]:
                newg[u].append((v, w))
                if v not in newg:
                    newg[v] = []
                newg[v].append((u, w))
        return newg

    def neighbors(self, node):
        return self.graph.get(node, [])

    def update_mask(self, mask, node):
        if node in self.goal_index:
            return mask | (1 << self.goal_index[node])
        return mask

    def is_goal_state(self, mask):
        return mask == self.ALL_MASK


class BestFirstMultiGoalAgent:
    def __init__(self, env):
        self.env = env

    def heuristic(self, node, mask):
        return 0

    def search(self):
        start = self.env.start
        start_mask = self.env.update_mask(0, start)

        frontier = [[0, 0, start, start_mask]]
        best_cost = {(start, start_mask): 0}
        parent = {(start, start_mask): None}

        while len(frontier) > 0:
            min_i = 0
            for i in range(1, len(frontier)):
                if frontier[i][0] < frontier[min_i][0]:
                    min_i = i

            f, cost, node, mask = frontier.pop(min_i)

            if cost != best_cost.get((node, mask), 10**18):
                continue

            if self.env.is_goal_state(mask):
                path = []
                cur = (node, mask)
                while cur is not None:
                    path.append(cur[0])
                    cur = parent[cur]
                path.reverse()
                return path, cost

            for nbr, w in self.env.neighbors(node):
                new_cost = cost + w
                new_mask = self.env.update_mask(mask, nbr)
                state = (nbr, new_mask)

                if state not in best_cost or new_cost < best_cost[state]:
                    best_cost[state] = new_cost
                    parent[state] = (node, mask)
                    frontier.append([new_cost + self.heuristic(nbr, new_mask), new_cost, nbr, new_mask])

        return None, None


def run_agent():
    env = MazeEnvironment(GRAPH, START, GOALS, undirected=True)
    agent = BestFirstMultiGoalAgent(env)
    path, cost = agent.search()

    if path:
        print("Final Path:", " -> ".join(path))
        print("Total Cost:", cost)
    else:
        print("No solution found.")


run_agent()
