from random import shuffle

def hill_climbing(problem):
    current = problem.initial()
    while True:
        neighbours = problem.nearStates(current)
        if not neighbours:
            break

        neighbour = max(neighbours, key=lambda state: problem.heuristic(state))
        if problem.heuristic(neighbour) <= problem.heuristic(current):
            break
        current = neighbour

    return current



def hc_rand_restart(problem, limit=10):
    state = problem.initial()
    count = 0
    while problem.goal_test(state) == False and count < limit:
        state = hill_climbing(problem)
        count += 1
    return state
