import random


def shuffle(problem, shuffles):
    initial = tuple(problem.goal)
    for i in range(0, shuffles):
        actions = problem.actions(initial)
        initial = problem.result(initial, random.choice(actions))
    return initial
