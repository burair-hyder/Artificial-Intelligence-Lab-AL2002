# markov model for weather 

import numpy as np

states = ['Sunny','Rainy']

transition_matrix = np.array([
    [0.8,0.2], # STATES FROM SUNNY
    [0.4,0.6]   # STATES FROM RAINY 
])


def simulate_weather_markov_model(initial_state,num_steps):
  current_state = initial_state
  state_sequence = [current_state]

  for _ in range(num_steps):

    if current_state == 'Sunny':
      next_state = np.random.choice(states,p=transition_matrix[0])
    else:
      next_state = np.random.choice(states,p=transition_matrix[1])
    
    state_sequence.append(next_state)
    current_state = next_state
  return state_sequence


int_state='Rainy'
steps=10
state_seq = simulate_markov_model(int_state,steps)
print("->".join(state_seq))
