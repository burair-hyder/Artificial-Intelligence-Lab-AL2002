# model based agent
# this agent performs action based on its internal memory + percept


class environment:
  
  def __init__(self,state):
    self.state = state

  def get_percept(self):
    return self.state
  
  def update_env(self,newpercept):
    self.state = newpercept
  
class modelbasedcleaner:

  def __init__(self):
    self.model = {}
  
  def updatemodel(self,percept):
    self.model['current'] = percept;
    print(self.model)

  def predictactionBasedOnModel(self):
    if self.model['current'] =="Dirty":
      return "Clean the Room"
    else:
      return "Room already Clean, Do nothing"

  def action(self,percept):
    self.updatemodel(percept)
    return self.predictactionBasedOnModel()

def agentprog(env,agent,steps):
  for step in range(steps):
    per = env.get_percept()
    action = agent.action(per)
    if action =="Clean the Room":
      env.update_env("Clean")
    print(f"Steps: {step} Current percept: {per}, Action : {action}")

env = environment("Dirty")
agent = modelbasedcleaner()
agentprog(env,agent,5)


# this agent does same as it is as simple reflex vacuum cleaner agent howeever it performs
# action based on its model and percept
# for eg in a window closer/opener program if windows needs to be closed and it is already 
# closed in the model , the agent chooses "DO nothing", instead of trying to close it again
    


