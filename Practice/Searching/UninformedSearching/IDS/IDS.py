# IDS 

# repeated DLS 

def DLS(node, goal , path ,depth):
  if depth == 0:
    return None
  if node == goal:
    path.append(node)
    return True

  for neighbour in tree[node]:
    if DLS(neighbour,goal,path,depth-1):
      path.append(node) # if at this node , the func returns true it means this node leads to the GOAL.
      return True
  return False

def IDS(start,goal,maxDepth):
  for depth in range(maxDepth+1):
    path  = []
    if DLS(start,goal,path,depth):
      print("Path: ", list(reversed(path)))   # basically reversed func produces a iterator ( and object which we can loop on)
                                              # it is not actual list , thus we cant print it directly ,
                                              # we need to convert it to a list using  " list()" func first.
      #print("Path: ",end=" ")
      #for node in reversed(path):
       # print(node,end="->")
      #print() 
      return True
  print("Path not found")
  return False;

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
result =IDS(startnode,goalnode,5)
print(result)
  
