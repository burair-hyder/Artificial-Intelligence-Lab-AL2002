# Question 03:

import random

def fitness(x):
    return x*x + 2*x

def to_decimal(binary):
    return int(binary, 2)

population = []

for i in range(6):
    chromosome = ""
    for j in range(5):
        chromosome += random.choice(['0','1'])
    population.append(chromosome)

for generation in range(15):

    fitness_values = []
    for c in population:
        x = to_decimal(c)
        fitness_values.append(fitness(x))

    new_population = []

    for _ in range(3):
        p1 = random.choice(population)
        p2 = random.choice(population)

        point = random.randint(1,4)

        child1 = p1[:point] + p2[point:]
        child2 = p2[:point] + p1[point:]

        if random.random() < 0.1:
            pos = random.randint(0,4)
            child1 = child1[:pos] + ('1' if child1[pos]=='0' else '0') + child1[pos+1:]

        if random.random() < 0.1:
            pos = random.randint(0,4)
            child2 = child2[:pos] + ('1' if child2[pos]=='0' else '0') + child2[pos+1:]

        new_population.append(child1)
        new_population.append(child2)

    population = new_population

best = population[0]
best_value = fitness(to_decimal(best))

for c in population:
    x = to_decimal(c)
    f = fitness(x)
    if f > best_value:
        best = c
        best_value = f

best_x = to_decimal(best)

print("Best Chromosome:", best)
print("Best value of x:", best_x)
print("Best fitness value:", best_value)
