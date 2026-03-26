# hill climbing 
graph = {
    'S': {'A': 3, 'B': 6, 'C': 5},
    'A': {'D': 9, 'E': 8},
    'B': {'F': 12, 'G': 14},
    'C': {'H': 7},
    'H': {'I': 5, 'J': 6},
    'I': {'K': 1, 'L': 10, 'M': 2},
    'D': {}, 'E': {}, 'F': {}, 'G': {},
    'J': {}, 'K': {}, 'L': {}, 'M': {}
}

heuristic = {
    'S': 10, 'A': 9, 'B': 7, 'C': 5, 'D': 8, 'E': 6, 'F': 4, 'G': 3,
    'H': 3, 'I': 2, 'J': 6, 'K': 2, 'L': 0, 'M': 1
}


def hillclimbing(graph,start,goal):
  current_node = start
  path = [current_node]
  
  while current_node != goal:
    neighbour = graph.get(current_node,[])
    if not neighbour:
      print("No path found via hill climbing")
      return None
    
    bestneighbour = min(neighbour,key = lambda x:heuristic[x[0]])
    bestneighbour_node = bestneighbour[0]

    if heuristic[bestneighbour_node] >= heuristic[current_node]:
      print("Stuck at local maxima")
      return
    
    current_node = bestneighbour_node
    path.append(current_node)

    if current_node == goal:
      print("Goal found using Hill Climbing,Path: ",path)
      return path


hillclimbing(graph,'S','L')
