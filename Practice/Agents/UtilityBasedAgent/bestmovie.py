# utility based agent 
# to select best movie based on utility = review * mood_factor


class environment:

  def __init__(self, movies=None):
    if movies is None:
      movies = {'Movie A':8, 'Movie B':7, 'Movie C':6, 'Movie D':5}
    self.movies = movies
  
  def get_percept(self):
    return self.movies



class utilitybasedAgent:

  def __init__(self,moodfactor = 0.7):
    self.moodfactor = moodfactor

  def calculateUtility(self,review):
    return self.moodfactor*review
  
  def act(self,percept):

    # now we have to select the best movie to watch based on utlity 
    bestmovie = None;
    bestutility = -999;

    for movie,review in percept.items():
      util = self.calculateUtility(review)
      if util > bestutility:
        bestutility = util
        bestmovie = movie
    return bestmovie
  
def agentprog(agent,env):
  per = env.get_percept();
  agent = utilitybasedAgent()
  bestmovie = agent.act(per)
  print(f"Available Movies: {per}")
  print(f"Best movie to watch: {bestmovie}")


env = environment();
agent = utilitybasedAgent()
agentprog(agent,env)
