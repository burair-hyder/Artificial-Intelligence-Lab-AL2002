#question 04
import numpy as np

states = ['Sunny', 'Cloudy', 'Rainy']
transition_matrix = np.array([
    [0.6, 0.3, 0.1],  
    [0.3, 0.4, 0.3],  
    [0.2, 0.3, 0.5]   
])

current_state = 0  # Sunny
weather_sequence = ['Sunny']

for _ in range(9):   
    current_state = np.random.choice([0, 1, 2], p=transition_matrix[current_state])
    weather_sequence.append(states[current_state])

print("Weather for 10 days:")

print(weather_sequence)


import numpy as np

states = ['Sunny', 'Cloudy', 'Rainy']
transition_matrix = np.array([
    [0.6, 0.3, 0.1],
    [0.3, 0.4, 0.3],
    [0.2, 0.3, 0.5]
])

num_simulations = 10000
count_at_least_3_rainy = 0

for _ in range(num_simulations):
    current_state = 0  
    rainy_days = 0

    for day in range(10):
        if current_state == 2:
            rainy_days += 1
        current_state = np.random.choice([0, 1, 2], p=transition_matrix[current_state])

    if rainy_days >= 3:
        count_at_least_3_rainy += 1

probability = count_at_least_3_rainy / num_simulations
print("Probability of at least 3 rainy days in 10 days:", probability)

