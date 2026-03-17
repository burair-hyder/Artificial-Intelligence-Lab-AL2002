# DFS + GOAL BASED AGENT
class environment:
  def __init__(self,graph,startnode):
    self.graph = graph
    self.startnode = startnode

  def get_graph(self):
    return self.graph

  def get_percept(self):
    return self.startnode
  
class GoalBasedDFSAgent:

  def __init__(self,goal):
    self.goal = goal
  
  def formulate_goal(self,percept):
    if percept == self.goal:
      return "Goal Found"
    else:
      return "Searching"
  
  def DFS(self,graph,startnode,goalnode):
    visited = []
    stack = []

    visited.append(startnode)
    stack.append(startnode)

    while stack:
      node = stack.pop()
      print(node,end= " ")

      if node == goalnode:
        return "\nGoal Found"

      for neighbours in reversed(graph[node]):
        if neighbours not in visited:
          visited.append(neighbours)
          stack.append(neighbours)
    return "dfs failed"

  def act(self,graph,percept):
    status = self.formulate_goal(percept)
    if status == "Goal Found":
      return "\nGoal Found"
    else:
      return self.DFS(graph,percept,self.goal)
    
def agentprog(env,agent):
  startnode = env.get_percept()
  action = agent.act(env.get_graph(),startnode)
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
goalnode = 'H'
env = environment(tree,startnode)
agent = GoalBasedDFSAgent(goalnode)
agentprog(env,agent)
