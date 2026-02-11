import random
class environment:
  
  def __init__(self,sPresent='Yes',Lightstatus ='Off'):
    self.sPresent = sPresent
    self.Lightstatus = Lightstatus

  def get_percept(self):
    return {
       'student_present': self.sPresent,
       'light_status': self.Lightstatus
    }
      
  def togglelights(self,stat):
    if (stat == 'Turn Lights off'):
      self.Lightstatus = 'Off'
    elif (stat == 'Turn Lights on'):
      self.Lightstatus = 'On'
  def randomize_presence(self):
        self.sPresent = random.choice(['Yes', 'No'])

  
class ModelAgent:
  def __init__(self):
    self.model = {
        'student_present': 'No',
        'light_status': 'Off'
    }
  def update_model(self,percept):
    self.model['student_present'] = percept['student_present']
    self.model['light_status'] = percept['light_status']

  
  def action(self,percept):
    if (self.model['student_present']=='Yes' and self.model['light_status']=='Off'):
      return 'Turn Lights on'
    elif self.model['student_present'] == 'No' and self.model['light_status'] == 'On' :
      return 'Turn Lights off'
    else:
      return 'No Action'  


def run_agent(agent,env,steps):
  for step in range(steps):
    env.randomize_presence()      
    percept = env.get_percept()
    agent.update_model(percept)
    action = agent.action(percept)
    print("Step:",step+1,"Percept:",percept,"-> Action:",action) 
    
    env.togglelights(action)
    
    

env = environment()
agent = ModelAgent()
run_agent(agent,env,8)
