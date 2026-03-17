# DFS CODE
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

def DFS(graph,start_node , goal_node):
  visited = []
  stack = []

  visited.append(start_node)
  stack.append(start_node)

  while stack:
    node = stack.pop()
    print(node,end=" ")

    if node == goal_node:
      print("\nGoal Found:",goal_node)
      print(f"Viisited: {visited}")
      print(f"Stack: {stack}")
      break
    
    for neighbours in reversed(graph[node]):
      if neighbours not in visited:
        stack.append(neighbours)
        visited.append(neighbours) 

start_node = 'A'
goal_node = 'H'

print("Applying DFS: ")
DFS(tree,start_node,goal_node)
