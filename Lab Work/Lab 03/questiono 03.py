# question 03 :


class environment:
  def __init__(self):
    self.sub = {
        "AI": False,
        "maths": False,
        "phy" : False
    }
class GoalBasedAgent:
  def __init__(self,goal):
    self.goal = goal
    self.finished = []
  
  def action(self,env):
    for subject in env.sub:
      if (env.sub[subject]==False):
        print("Studying" , subject)
        env.sub[subject] = True
        self.finished.append(subject)
  
    if (len(self.finished)==3):
      return True
    else:
      return False

def run_agent(agent, env):
  
    goal_completed = False
    while not goal_completed:
      
        goal_completed = agent.action(env)
    print("Goal Achieved: All subjects completed")


env = environment()
agent = GoalBasedAgent("Complete all subjects")
run_agent(agent, env)
          
