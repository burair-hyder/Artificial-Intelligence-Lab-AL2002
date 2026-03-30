import random


def queenfitness(board):
  non_attacking_pairs =0
  totalpairs = n *(n-1)/2

  for row in range(n):
    for col in range(row+1,n):
      if (board[row]!= board[col]) and abs(row-col) == abs(board[row]- board[col]):
        non_attacking_pairs += 1
  return non_attacking_pairs  


def create_board():
  return random.sample(range(n),n)
  # creates a list of size n (range n ) and does permutation of 0 to n-1





# calculating fitness score for each sample



def selection_parents(population,fitness_score):
# selection top 50%
    paired= list(zip(fitness_score,population))
  #  print(paired)

    # we neeed to sort
    paired.sort(reverse = True)

    print(paired)

    sorted_population = []
    for fitness,pop in paired:
      sorted_population.append(pop)
 #   print(sorted_population[:len(sorted_population)//2])
    return sorted_population[:len(sorted_population)//2]





def crossover(parent1, parent2):
  point = random.randint(1,n-2)
  child = parent1[:point] + parent2[point:]

  # howeever this child can have duplicates
  # we need to find the missing values
  missing = set(range(n))-set(child)

  for i in range(len(child)):
    if (child.count(child[i])>1):
      child[i]= missing.pop()
  return child
  



def mutate(board):
  idx1,idx2 = random.sample(range(n),2)
  board[idx1],board[idx2] = board[idx2],board[idx1]
  return board

mutation_rate = 0.1  # a chance of 10% to mutate
n=4
population_size=10
def ga_Queen_Solver():
  population = []
  generation = 0
  best_fitness = 0
  max_fitness  = n*(n-1)//2;

  # intilializing population

  for i in range(population_size):
    ind = create_board();
    population.append(ind)


  # main loop
  # untill we solve it (get max fitness) or generation becomes greater than 100

  while best_fitness < max_fitness and generation <100:
      fitness_score = []
      for ind in population:
        score = queenfitness(ind)
        fitness_score.append(score)
      best_fitness = max(fitness_score)
      print(f"Generation : {generation} Best Fitness: {best_fitness}")

      if best_fitness == max_fitness:
        finalgene =list(zip(fitness_score,population))
        finalgene.sort(reverse=True)
        print("Final gene: ",finalgene)
        break
        
        # we need to perform GA 
        # select parents top 50 %
      parents = selection_parents(population,fitness_score)

      new_population=[]
      for i in range(population_size):
        parent1,parent2 = random.sample(parents,2)
        child = crossover(parent1,parent2);
        new_population.append(child)
        

      for i in range(len(new_population)):
        if random.random()<mutation_rate:
          new_population[i] = mutate(new_population[i])

        
      population = new_population
      generation +=1
    
  best_ind = max(population, key=queenfitness)
  return best_ind , queenfitness(best_ind)



      

solution, fitness = ga_Queen_Solver()
print("Best Solution:", solution)
print("Best Fitness:", fitness)

  


 
