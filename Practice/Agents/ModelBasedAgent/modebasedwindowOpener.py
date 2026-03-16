
class environment:
  def __init__(self,rain,windowstatus):
    self.rain = rain
    self.windowstatus = windowstatus

  def get_percept(self):
    return {'rain': self.rain, 'windowstatus': self.windowstatus}

  def close_window(self):
    if self.windowstatus == 'Open':
      self.windowstatus = 'Closed'

    

class modelbasedagent:

  def __init__(self):
    self.model = {}

  def updatemodel(self,percept):
    self.model = percept
  
  def act(self,percept):
    self.updatemodel(percept)

    if self.model['rain'] == 'Yes' and self.model['windowstatus'] == 'Open':
      return 'Close the window'
    else:
      return 'no action neeeded'
  

def agentprog(env,agnet,steps):
  for step in range(steps):
    per = env.get_percept()
    action=  agent.act(per)
    if action == 'Close the window':
      env.close_window()
    print(f"Steps: {step} Percept: {per}, Action: {action}")



env = environment('Yes','Open')
agent = modelbasedagent()
agentprog(env,agent,5)



