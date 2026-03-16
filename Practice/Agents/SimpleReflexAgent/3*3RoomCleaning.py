from os import environ
# simple reflex agent 
# 3X3 room 

class environment:
  def __init__(self):
    self.room  = [ ['Clean','Dirty','Clean'],
                   ['Clean','Dirty','Dirty'],
                   ['Clean','Clean','Clean'] 
                 ]
  def get_percept(self,x,y):
    if self.room[x][y] == 'Clean':
      return "Clean."
    else:
      return "Dirty."

  def clean_room(self,x,y):
    self.room[x][y] = "Clean"
  
  def printroom(self,x,y):
    #copy = self.room.copy()
    copy = [row[:] for row in self.room]  # making deep copy 
    #  [:] is used to deep copy every element of a list
    #  a = [1, 2, 3, 4]
    #  b = a[:]      # copy all elements
    #  b[0] = 100
    #  print(a)      # [1, 2, 3, 4]  ✅ original unchanged
    #  print(b)      # [100, 2, 3, 4]
    # but if we have did b=a changing b also changes a 
    # in this senario it copies row[:] for every row in self.room
    copy[x][y] = 'Agent'
    for i in range(3):
      for j in range(3):
        print(copy[i][j],end =" ")
      print()

class simplereflexRoomCleaner:
  def __init__(self):
    self.x = 0
    self.y = 0
  
  
  def act(self,percept):
    if percept == 'Clean.':
      return "Room already Clean, Do nothing."
    else:
      return "Clean the Room."

  def movagent(self):
    if self.y < 2:
      self.y = self.y + 1
    else:
      self.y = 0
      if self.x < 2:
        self.x = self.x +1



def agentprog(env,agent,steps):
  for step in range(steps):
    per = env.get_percept(agent.x,agent.y)
    act = agent.act(per)
    if (act =="Clean the Room."):
      env.clean_room(agent.x,agent.y)
    print(f"Step: {step} Current percept: {per} Action : {act}")
    env.printroom(agent.x,agent.y)
    agent.movagent()

env = environment()
agent = simplereflexRoomCleaner();
agentprog(env,agent,9);
        
          
