import math
class Node:

  def __init__(self,value):
    self.value = value
    self.children = []
    self.minimax_value = None

# the internal nodes have labels "A B C" as self.value
# the leaf nodes have actuall numbers as self.value



class Environement:

  def __init__(self,tree):
    self.tree = tree # stores the root node of tree
    self.computed_nodes = []  # to show the DFS Order 

  def get_percept(self,node):
    return node

  def compute_minimax(self,node,depth,maximizing_player = True):

    if depth == 0 or not node.children:
      self.computed_nodes.append(node.value)
      return node.value

    if maximizing_player==True:
      best = -math.inf
      for child in node.children:
        child_value = self.compute_minimax(child,depth-1,False)
        best = max(best,child_value)
        
      node.minimax_value = best
      self.computed_nodes.append(node.value)
      return best

    else:
      best = math.inf
      for child in node.children:
        child_value = self.compute_minimax(child,depth-1,True)
        best = min(best,child_value)
      node.minimax_value= best
      self.computed_nodes.append(node.value)
      return best


class MinimaxAgent:
  def __init__(self,depth):
    self.depth = depth
    # the agent should know how deep to go
  
  def formulate_goal(self,node):
    if node.minimax_value is not None:
      return "Goal Reached."
    else:
      return "Searching."
  
  def act(self,node,env):
    goal_check = self.formulate_goal(node)

    if goal_check == "Goal Reached.":
      return f"Minimax Value for root Node is: {node.minimax_value}"
    else:
      return env.compute_minimax(node,self.depth)



def agent_prog(agent,env):
  percept = env.get_percept(env.tree)
  act = agent.act(percept,env)
  return  act



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
# define depth for Minimax
depth = 3


agent = MinimaxAgent(depth)
env = Environement(root)

res =agent_prog(agent,env)

print("Minimax Values:")
print("Value at Root Node:", root.minimax_value)
print("Returned Result:", res)
print("Computed Nodes:", env.computed_nodes)

  
