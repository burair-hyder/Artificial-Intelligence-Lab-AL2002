# another utility based agent 
# it also considers agents mood , review and type of movie to decide which one to watch

class environment:
  def __init__(self,movies = None):
    if movies is None:
      movies = {
                  'Movie A': {'rating': 8, 'type': 'fun'},
                  'Movie B': {'rating': 9, 'type': 'serious'},
                  'Movie C': {'rating': 7, 'type': 'fun'}
              }
    self.movies = movies
  
  def get_percept(self):
    return self.movies

class utilitybasedAgent:
    
    def __init__(self,moodfactor = 0.7):
      self.moodfactor = moodfactor
    
    def calUtility(self,review,type):
      moodbonus = 0
      if type == 'fun':
        moodbonus = self.moodfactor *3
      else: 
        moodbonus = (1- self.moodfactor)*3
      return review + moodbonus

    def act(self,percept):
      bestmovie = None
      bestutility = -999

      for movie,info in percept.items():
        utility = self.calUtility(info['rating'],info['type'])
        if utility > bestutility:
          bestutility = utility
          bestmovie = movie
      return bestmovie

def agentprog(agent,env):
  per = env.get_percept()
  bestmovie = agent.act(per)

  print(f"Available Movies: {per}")
  print(f"Mood factor : {agent.moodfactor}")
  print(f"Best movie to watch: {bestmovie}")
  



env = environment()

print("Sadd Agent:")
sadagent = utilitybasedAgent(0.3)
agentprog(sadagent,env)
print()

print("Happpy Agent:")
happyagent = utilitybasedAgent(0.9)
agentprog(happyagent,env)



