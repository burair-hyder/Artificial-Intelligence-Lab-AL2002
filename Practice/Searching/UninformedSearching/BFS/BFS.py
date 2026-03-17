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
"""-> BFS functions accepts a graph, start node, goal node 
   1) it has a list (array) to store the visited nodes
   2) it has a queue structure to store nodes to explore  
   3) the start node is added to both, the visited list and the queue
	THE SEARACH CONTINUES AS LONG AS WE HAVE NODES IN THE QUEUE
	
   REPEAT:
   4)   - dequeue from front of queue
	- is node = goal then stop search and return
	- else : enqueue all neighbours(childs) of that node
	- stop if all nodes are explored. """




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
