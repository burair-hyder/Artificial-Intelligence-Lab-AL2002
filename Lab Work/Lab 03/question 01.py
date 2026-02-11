# question 1 :

class environment:
  def __init__(self,trafficStat):
    self.trafficStat = trafficStat

  def get_percept(self):
    return 'Heavy Traffic' if self.trafficStat == 'Heavy' else 'Light Traffic'
  
class ReflexAgent:
  def __init__(self):
    pass
  def action(self,percept):
    if (percept=="Heavy Traffic"):
      return "Green for longer"
    else:
      return "Normal Green"

def run_agent(env,agent):
  action = agent.action(env.get_percept())
  print("Percept:",env.get_percept(),"-> Action:",action)


env = environment('Heavy')
agent = ReflexAgent()
run_agent(env,agent)
  
env1 = environment('Light')
run_agent(env1,agent)
