# Question 01:

import random

def f(x):
    return -x**2 + 6*x

x = random.randint(0,6)
print("Initial x:", x)
print("f(x):", f(x))

while True:
    neighbors = []
    
    if x-1 >= 0:
        neighbors.append(x-1)
    if x+1 <= 6:
        neighbors.append(x+1)

    best = x
    
    for n in neighbors:
        if f(n) > f(best):
            best = n

    if best == x:
        break

    x = best
    print("Move to x:", x, "f(x):", f(x))

print("Final Optimal x:", x)
print("Final Optimal f(x):", f(x))
