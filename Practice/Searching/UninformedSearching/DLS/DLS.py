# DLS  = DFS + DEPTH LIMIT + BACKTRACKING (recursion)

def DLS(graph,start,goal,depth_limit):
  visited = []

  def DFS(node,depth):

    if depth > depth_limit:
      return None
    visited.append(node)
    if node == goal:
      return visited.copy()
  
    for neighbours in graph[node]:
      if neighbours not in visited:
        path = DFS(neighbours,depth+1)
        if path:
          return path
    visited.pop()
    return None
  
  finalpath = DFS(start,0)

  if finalpath:
    print( "Goal Found using DLS.",finalpath)
  else:
    print("Goal Not Found using DLS.")
  return finalpath


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
startnode = 'A'
goalnode = 'H'
print("Depth Limit 2")
path  = DLS(tree,startnode,goalnode,2)
print(path)

print()
print("Depth Limit 3")
path  = DLS(tree,startnode,goalnode,3)
print(path)




