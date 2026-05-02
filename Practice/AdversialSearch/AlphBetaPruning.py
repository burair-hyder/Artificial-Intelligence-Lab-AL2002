# proper agent based code of alpha beta pruning 

import math
class Node:
  def __init__(self,value):
    self.value = value
    self.children = []
    self.minimax_value= None



class AlphaBetaAgent:
# the agent should have depth, goalformulate, act 
  def __init__(self,depth):
    self.depth = depth
  
  def formulate_goal(self,node):
    # check is node has a minimax value 
    if node.minimax_value is not None:
      return "Goal Found"
    else:
      return "Searching"
  def act(self,node,env):
    goalcheck = self.formulate_goal(node)
    if goalcheck == "Goal Found":
      return f"Minimax Value at Root: {node.minimax_value}"
    else:
      return env.alpha_beta_pruning(node,self.depth,-math.inf,math.inf)

class Environment:
  def __init__(self,tree):
    self.tree= tree # this will hold the root node
    self.computed_nodes = []

  def get_percept(self):
    return self.tree

  def alpha_beta_pruning(self,node,depth,alpha,beta,maximizing_player=True):

    if depth == 0 or not node.children:
      self.computed_nodes.append(node.value)
      return node.value 
      
    if maximizing_player==True:
      best = -math.inf

      for child in node.children:
        child_value = self.alpha_beta_pruning(child,depth-1,alpha,beta,False)
        best = max(best,child_value)
        alpha = max(best,alpha)

        if alpha >= beta:
            # prune 
          print("Pruned after the Node:",child.value)
          break
        
      node.minimax_value = best
      self.computed_nodes.append(node.value)
      return best

          
    else:
      best = math.inf

      for child in node.children:
        child_value = self.alpha_beta_pruning(child,depth-1,alpha,beta,True)
        best = min(best,child_value)
        beta = min(best,beta)

        if alpha >=beta:
            # prune
          print("pruned after child: ",child.value)
          break

      node.minimax_value = best
      self.computed_nodes.append(node.value)
      return best

          
def agentprog(agent,env):
  percept = env.get_percept()
  act = agent.act(percept,env)
  return act


root = Node('A')

n1 = Node('B')
n2 = Node('C')
root.children = [n1, n2]

n3 = Node('D')
n4 = Node('E')
n5 = Node('F')
n6 = Node('G')

n1.children = [n3, n4]
n2.children = [n5, n6]

n7 = Node(2)
n8 = Node(3)
n9 = Node(5)
n10 = Node(9)

n3.children = [n7, n8]
n4.children = [n9, n10]

n11 = Node(0)
n12 = Node(1)
n13 = Node(7)
n14 = Node(5)

n5.children = [n11, n12]
n6.children = [n13, n14]


# Define depth
depth = 3

# Create agent and environment
agent = AlphaBetaAgent(depth)
environment = Environment(root)

# Run agent
result = agentprog(agent, environment)

# Output
print("Returned Result:", result)
print("Computed Nodes:", environment.computed_nodes)

print("Minimax values:")
print("A:", root.minimax_value)
print("B:", n1.minimax_value)
print("C:", n2.minimax_value)
print("D:", n3.minimax_value)
print("E:", n4.minimax_value)
print("F:", n5.minimax_value)
print("G:", n6.minimax_value)
      


