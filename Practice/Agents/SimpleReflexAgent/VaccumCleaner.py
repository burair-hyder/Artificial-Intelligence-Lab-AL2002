# simple reflex agent 
# vaccum cleaner
import random 

class environment:
  def __init__(self):
    num = random.randint(0,1);
    if num==0:
      self.state = "clean"
    else:
      self.state = "dirty"

  def get_percept(self):
    return self.state

  def update_env(self,newpercept):
    self.state = newpercept

  def update_env_random(self):
    num = random.randint(0,1);
    if num==0:
      self.state = "clean"
    else:
      self.state = "dirty"
  
class simplereflexCleaner:
  def __init__(self):
    pass
  
  def action(self,percept):
    if percept == "clean":
      return "Room already Clean, Do nothing."
    else:
      return "Clean the Room."

def agentprog(env,agent,steps):
  for step in range(steps):
    per = env.get_percept()
    action = agent.action(per)
    if action =="Clean the Room.":
      env.update_env("clean")
    print(f"Current percept: {per} Action : {action}")
    env.update_env_random();


env = environment()
agent = simplereflexCleaner()
agentprog(env,agent,5)

