# A* Search

# graph will contain nodes and cost (g)
# heuristic list will contain the (h) (forward cost)


graph = {
 'A': {'B': 4, 'C': 3},
 'B': {'E': 12, 'F': 5},
 'C': {'D': 7, 'E': 10},
 'D': {'E': 2},
 'E': {'G': 5},
 'F': {'G': 16},
 'G': {},
}
heuristic = {'A': 14,'B': 12,'C': 11,'D': 6,'E': 4,'F': 11,'G': 0 }

def A_star(graph,start_node,goal_node):
  g_cost = {start_node : 0}
  frontier = [(start_node,0 + heuristic[start_node])]
  came_from = {start_node : None}
  visited = set()

  while frontier:
    frontier.sort(key=lambda x:x[1])
    current_node,currentF = frontier.pop(0)

    if current_node in visited:
      continue
    
    visited.add(current_node)

    if current_node == goal_node:
      path =[]
      while current_node is not None:
        path.append(current_node)
        current_node = came_from[current_node]
      path.reverse()
      print("Goal Foud using A*, Path Found:",path)
      return
    

    for neighbour,costg in graph[current_node].items():
      newg = costg+ g_cost[current_node]
      fcost = newg + heuristic[neighbour]
      if neighbour not in g_cost or newg < g_cost[neighbour]:
        g_cost[neighbour] =newg
        came_from[neighbour] = current_node
        frontier.append((neighbour,fcost))
  
  print("Goal Not found")
  return False

A_star(graph,'A','G')




