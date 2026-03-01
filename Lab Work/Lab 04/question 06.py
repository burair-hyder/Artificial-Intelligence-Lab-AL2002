# Question 06:
import random

graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}

h = {'A': 14, 'B': 12, 'C': 11, 'D': 6, 'E': 4, 'F': 11, 'G': 0}

START = 'A'
GOAL = 'G'
INF = 10**18


class LPAStar:
    def __init__(self, graph, h, start, goal):
        self.graph = graph
        self.h = h
        self.start = start
        self.goal = goal

        self.nodes = set(graph.keys())
        for u in graph:
            for v in graph[u]:
                self.nodes.add(v)

        self.pred = {n: [] for n in self.nodes}
        for u in graph:
            for v in graph[u]:
                self.pred[v].append(u)

        self.g = {n: INF for n in self.nodes}
        self.rhs = {n: INF for n in self.nodes}
        self.bp = {n: None for n in self.nodes}
        self.open = []

        self.rhs[self.start] = 0
        self._push(self.start)

    def _k(self, n):
        m = self.g[n] if self.g[n] < self.rhs[n] else self.rhs[n]
        return (m + self.h.get(n, 0), m)

    def _in_open(self, n):
        for i in range(len(self.open)):
            if self.open[i][2] == n:
                return i
        return -1

    def _remove_open(self, n):
        i = self._in_open(n)
        if i != -1:
            self.open.pop(i)

    def _push(self, n):
        self._remove_open(n)
        self.open.append([self._k(n), self.h.get(n, 0), n])

    def _pop_min(self):
        mi = 0
        for i in range(1, len(self.open)):
            if self.open[i][0] < self.open[mi][0]:
                mi = i
        return self.open.pop(mi)[2]

    def update_vertex(self, v):
        if v != self.start:
            best = INF
            best_p = None
            for p in self.pred.get(v, []):
                if v in self.graph.get(p, {}):
                    val = self.g[p] + self.graph[p][v]
                    if val < best:
                        best = val
                        best_p = p
            self.rhs[v] = best
            self.bp[v] = best_p

        self._remove_open(v)
        if self.g[v] != self.rhs[v]:
            self._push(v)

    def compute_shortest_path(self):
        while True:
            if len(self.open) == 0:
                break
            top = self.open[0][0]
            for i in range(1, len(self.open)):
                if self.open[i][0] < top:
                    top = self.open[i][0]

            goal_key = self._k(self.goal)
            if not (top < goal_key or self.rhs[self.goal] != self.g[self.goal]):
                break

            u = self._pop_min()
            if self.g[u] > self.rhs[u]:
                self.g[u] = self.rhs[u]
                for s in self.graph.get(u, {}):
                    self.update_vertex(s)
            else:
                self.g[u] = INF
                self.update_vertex(u)
                for s in self.graph.get(u, {}):
                    self.update_vertex(s)

    def path_and_cost(self):
        if self.g[self.goal] >= INF:
            return None, None

        path = []
        cur = self.goal
        seen = set()
        while cur is not None:
            if cur in seen:
                return None, None
            seen.add(cur)
            path.append(cur)
            if cur == self.start:
                break
            cur = self.bp[cur]

        if len(path) == 0 or path[-1] != self.start:
            return None, None

        path.reverse()
        return path, self.g[self.goal]

    def change_edge_cost(self, u, v, new_cost):
        if u not in self.graph:
            self.graph[u] = {}
        self.graph[u][v] = new_cost
        if v not in self.pred:
            self.pred[v] = []
        if u not in self.pred[v]:
            self.pred[v].append(u)
        self.update_vertex(v)

    def edges(self):
        ed = []
        for u in self.graph:
            for v in self.graph[u]:
                ed.append((u, v))
        return ed


def run_dynamic_astar(steps=5, delta_choices=(-4, -3, -2, -1, 1, 2, 3, 4)):
    planner = LPAStar(graph, h, START, GOAL)
    planner.compute_shortest_path()

    p, c = planner.path_and_cost()
    print("Initial Path:", " -> ".join(p) if p else "None")
    print("Initial Cost:", c)

    eds = planner.edges()

    for t in range(1, steps + 1):
        u, v = random.choice(eds)
        old = planner.graph[u][v]
        d = random.choice(delta_choices)
        new = old + d
        if new < 1:
            new = 1

        planner.change_edge_cost(u, v, new)
        planner.compute_shortest_path()

        p, c = planner.path_and_cost()
        print("\nUpdate", t, ":", u + "->" + v, old, "->", new)
        print("Path:", " -> ".join(p) if p else "None")
        print("Cost:", c)

    #return planner


run_dynamic_astar(steps=6)
