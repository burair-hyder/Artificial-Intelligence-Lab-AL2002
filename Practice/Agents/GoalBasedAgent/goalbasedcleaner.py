# goal based agent
# this means that agent will have a goal to set and acheive by acting


class environment:

  def __init__(self,state = 'Dirty'):
    self.state = state

  def get_percept(self):
    return self.state

  def update_env(self,newstate):
    self.state = newstate


class goalbasedAgent:

  def __init__(self):
    goal = 'Clean'
  
  def formulate_goal(self,percept):
    if percept == 'Dirty':
      self.goal = "Clean Room"
    else:
      self.goal = "No action required"
    
  def act(self,percept):
    self.formulate_goal(percept)
    if self.goal == "Clean Room":
      return "Clean the Room"
    else:
      return "No action required"


def agentprog(env,agent,steps):

  for step in range(steps):
    per = env.get_percept()
    action = agent.act(per)
    if action == "Clean the Room":
      env.update_env("Clean")
    print(f"Steps: {step} Percept: {per}, Action: {action}")

env = environment()
agent = goalbasedAgent()
agentprog(env,agent,5)


