# Question 02:

goal = 20
beam_width = 2

def h(n):
    return abs(goal - n)

beam = [(1, [1])]
visited = set([1])
level = 0

while beam:
    print("Level", level, ":", [state for state, path in beam])

    new_states = []

    for state, path in beam:

        next_states = [state + 2, state + 3, state * 2]

        for n in next_states:
            if n <= goal and n not in visited:
                visited.add(n)
                new_states.append((n, path + [n]))

    new_states.sort(key=lambda x: h(x[0]))
    beam = new_states[:beam_width]

    for state, path in beam:
        if state == goal:
            print("Final Path:", path)
            exit()

    level += 1
