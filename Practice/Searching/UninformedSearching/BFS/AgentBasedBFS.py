class environment:
  def __init__(self,tree,startnode):
    self.tree = tree
    self.startnode = startnode
    
  
  def get_graph(self):
    return self.tree

  def get_percept(self):
    return self.startnode

class GoalBasedBFSAgent:

  def __init__(self,goal):
    self.goal = goal

  def formulate_goal(self,percept):
    if self.goal == percept:
      return "Goal Found"
    else:
      return "Searching"


  def BFS(self,graph,startnode,goalnode):
    visited = []
    queue = []

    visited.append(startnode)
    queue.append(startnode)

    while queue:
      node = queue.pop(0)
      print(node,end =" ")

      if node == goalnode:
        return "\nGoal Found"

      for neighbours in graph[node]:
        if neighbours not in visited:
          queue.append(neighbours)
          visited.append(neighbours)
    return "bfs failed"      

  def act(self,graph,percept):
    status = self.formulate_goal(percept)
    if status == "\nGoal Found":
      return "\nGoal Found"
    else:
      return self.BFS(graph,percept,self.goal)

def agentprog(agent,env):
  graph = env.get_graph()
  percept = env.get_percept()

  action = agent.act(graph,percept)
  print(action)

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
env = environment(tree,startnode)
agent = GoalBasedBFSAgent('H')
agentprog(agent,env)

