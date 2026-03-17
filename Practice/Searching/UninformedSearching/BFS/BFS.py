tree = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : ['H'],
    'E' : ['I'],
    'F' : [],
    'G' : [],
    'H' : [],
    'I' : []
}


def BFS(graph,start,goal):
  visited = []
  queue = []

  visited.append(start)
  queue.append(start)

  while queue:
    node = queue.pop(0)
    print(node,end=" ")

    if node == goal:
      print("\nGoal Found:",node)
      print(visited)
      print(queue) 
      break

    for neighbours in graph[node]:
      if neighbours not in visited:
        queue.append(neighbours)
        visited.append(neighbours)


start_node = 'A'
goal_node  =  'H'

print("Applying BFS: ")
BFS(tree,start_node,goal_node)
