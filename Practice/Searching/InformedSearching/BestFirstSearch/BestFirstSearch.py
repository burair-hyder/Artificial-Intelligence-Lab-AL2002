from os import truncate
# INFORMED SEARCHES
# BFS  (BEST FIRST SEARCH)
# USES HEURISTIC ( INDRECTION OF GOAL)
from queue import PriorityQueue
def BestfirstSearch(graph,start_node,goal_node):
  visited = set()
  pq = PriorityQueue()
  pq.put((0,start_node))
  came_from = {start_node:None}

  while not pq.empty():
    cost,current_node = pq.get()
    if current_node not in visited:
      visited.add(current_node)
      print(current_node,end=" ")
      if current_node == goal_node:
        path = []
        while current_node is not None:
          path.append(current_node)
          current_node = came_from[current_node]
        path.reverse()
        print("\nGoal Reached, Path:",path)
        return True
      
      for neighbour,weight in graph[current_node]:
        if neighbour not in visited:
          if neighbour  not in came_from:
            came_from[neighbour]=current_node
            pq.put((weight,neighbour))

  print("Goal not reached")
  return False
graph = {
 'S': [('A', 3), ('B', 6), ('C', 5)],
 'A': [('D', 9), ('E', 8)],
 'B': [('F', 12),('G', 14)],
 'C': [('H', 7)],
 'H': [('I', 5), ('J', 6)],
 'I': [('K', 1),('L', 10), ('M', 2)],
 'D': [],
 'E': [],
 'F': [],
 'G': [],
 'J': [],
 'K': [],
 'L': [],
 'M': []
}

print("Best-First Search Path:")
BestfirstSearch(graph, 'S', 'I')
