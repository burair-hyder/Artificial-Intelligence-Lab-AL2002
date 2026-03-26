import random
def calculate_conflicts(state):
  print(state)
  conflicts = 0
  n = len(state)
  for row in range(n):
    for col  in range(row+1,n):
      if state[row] == state[col] or abs(state[row]-state[col]) == abs(row-col):
        conflicts = conflicts +1
  return conflicts

def get_neighbours(state):
  n = len(state)
  neigbours =[]
  for row in range(n):
    for col in range(n):
      if state[row] != col:
        new_state = list(state)
        new_state[row] = col
        neigbours.append(new_state)
  return neigbours


def nQueen_hillClimb(n):
  # gen current state
  current_state = [random.randint(0, n - 1) for _ in range(n)]
  current_conflicts = calculate_conflicts(current_state)

  while True:
    neighbours = get_neighbours(current_state)
    next_state = None
    next_conflicts = current_conflicts

    for neighbour in neighbours:
      nconflicts = calculate_conflicts(neighbour)
      if nconflicts < next_conflicts:
        next_state=  neighbour
        next_conflicts = nconflicts
        break
    
    if next_conflicts >= current_conflicts:
      break
    
    current_state = next_state
    current_conflicts = next_conflicts
  return current_state, current_conflicts
n = 8  
solution, conflicts = nQueen_hillClimb(4)


# Print results
if conflicts == 0:
    print(f"Solution found for {n}-Queens problem:")
    print(solution)
else:
    print(f"Could not find a solution. Stuck at state with {conflicts} conflicts:")
    print(solution)
