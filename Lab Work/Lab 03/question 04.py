class environment:
  def __init__(self,name,distance,rating):
    self.name = name
    self.distance = distance
    self.rating = rating
  
class UtilityBasedAgent:
  def calUtility (self,distance,rating):
    return rating -distance
  
  def act(self,rest1,rest2):
    utility1 = self.calUtility(rest1.distance,rest1.rating);
    utility2 = self.calUtility(rest2.distance,rest2.rating);

    print ("Resturant",rest1.name,"Utility:",utility1)
    print ("Resturant",rest2.name,"Utility:",utility2)

    if (utility1 >= utility2):
       selected = rest1.name
    else:
      selected = rest2.name
    return selected


def run_agent(agent,rest1,rest2):
  choice = agent.act(rest1,rest2)
  print("Selected Resturant:",choice)
        
rest1 = environment('A',3,7)
rest2 = environment('B',5,9)
agent = UtilityBasedAgent()
run_agent(agent,rest1,rest2)
