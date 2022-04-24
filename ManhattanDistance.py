def manhattanDistance(state, goal):
    man_dist = 0
    for i in range(0, len(state)):
        if state[i] != 0:
            j = goal.index(state[i])
            man_dist += abs(j // 4 - i // 4) + abs(j % 4 - i % 4)
    return man_dist
