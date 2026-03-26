# UCS (Uniform Cost Search)
# parameters : graph ,startnode,goalnode
# structures used : frontier,visited,cost_tillnow,came_from
# loop untill frontier
# sort frontier
# pop(0) to get cheapest node
# this becomes currentnode and its cost is current_cost
# if it is goal, reconstruct path using came_from and currentnode
# if not, traverse its neighbour 
# check if neighbour is already visited 
# if not then check its new cost and whether it is in cost_tillnow or newcost is less than previouse one
# if yes then append to frontier, update cost_tillnow and came_from dictory for this neighbour



def UCS(graph,start_node,goal_node):
  frontier = [(start_node,0)]
  cost_so_far = {start_node:0}
  came_from ={start_node:None}
  visited= set()

  while frontier:
    frontier.sort(key=lambda x:x[1])

    current_node,current_cost = frontier.pop(0)

    if current_node in visited:
      continue
    
    visited.add(current_node) # why not append ?

    if current_node == goal_node:
      # found goal , reconstruct path
      path=[]
      while current_node is not None:
        path.append(current_node)
        current_node = came_from[current_node]
      path.reverse()
      print(f"Goal Found! with Path : {path} and Total Cost: {current_cost}")
      return 
    

    # goal not found traverse the neigbours
    for neighbour,cost in graph[current_node].items():
      newcost = current_cost + cost
      if neighbour not in cost_so_far or newcost < cost_so_far[neighbour]:
        cost_so_far[neighbour ] = newcost
        came_from[neighbour] = current_node
        frontier.append((neighbour,newcost))  

  print(f"Goal not Found") 
  return None   


graph = {
 'A': {'B': 2, 'C': 1},
 'B': {'D': 4, 'E': 3},
 'C': {'F': 1, 'G': 5},
 'D': {'H': 2},
 'E': {},
 'F': {'I': 6},
 'G': {},
 'H': {},
 'I': {}
}
UCS(graph, 'A', 'I')
