# BEAM search
# beam will store possible paths and their cost
# it will work like bfs ...but at each level it only stores only best k paths
import heapq

graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'D': [], 'E': [],
    'F': [], 'G': [],
    'J': [], 'K': [],
    'L': [], 'M': []
}
def beamSearch(beamWidth,graph,start,goal):
  beam = [(0,[start])]

  while beam:
    candidates =[]

    for cost,path in beam:
      current_node = path[-1]

      if current_node == goal:
        return path,cost

      for neighbour,edgecost in graph[current_node]:
        newcost = cost + edgecost
        newpath = path + [neighbour]
        candidates.append((newcost,newpath))
    
    beam = heapq.nsmallest(beamWidth,candidates,key=lambda x:x[0])
  return None,float('inf')


start_node = 'S'
goal_node = 'L'
beam_width = 3

path, cost = beamSearch(beam_width,graph,start_node,goal_node)
print("Path:", path)
print("Cost:", cost)
