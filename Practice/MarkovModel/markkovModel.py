# MARKOV MODEL
import numpy as np

# DEFINE STATES AND TRANSITION MATRIX 
states =['Red','Blue']

# IT TELLS PROBAB OF MOVING FROM ONE STATE TO ANOTHER 
transition_matrix = np.array([
    # R  B
    [0.5,0.5],   # FROM RED -> RED OR BLUE
    [0.5,0.5]    # FROM BLUE -> RED OR BLUE
])

def simulate_markov_model(intital_state,num_steps):
  # INTIAL_STATE IS THE STARTING POINT
  # NUM_STEMPS -> how many steps to simulate

  current_state = intital_state
  state_sequence = [current_state]

  for _ in range(num_steps):

    if current_state == 'Red':
      next_state = np.random.choice(states,p=transition_matrix[0])
    else:
      # current_state == Blue 
      # pass the index 1 of transition matrix telling prob of sates from BLUE
      next_state = np.random.choice(states,p=transition_matrix[1])

    state_sequence.append(next_state)
    current_state = next_state
  return state_sequence
  
initial_state = 'Red'
num_steps = 10

state_sequence = simulate_markov_model(initial_state,num_steps)
for state in state_sequence:
  print(state,end="->")
   


