import matplotlib.pyplot as plt
from FifteenPuzzleProblem import FifteenPuzzle
from Astar import astar_search
from BidirectionalAstar import astar_bidirectional_search
from Shuffle import shuffle
import statistics
import numpy as np


def test():
    x = []

    path_LC = []
    path_bi_LC = []
    explored_LC = []
    explored_bi_LC = []
    shuf = 20
    for i in range(0, 100):
        problem = FifteenPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))
        if i % 10 == 0:
            shuf += 5
            x.append(shuf)
        initial_state = shuffle(problem, shuf)
        problem = FifteenPuzzle(initial_state, 'LinC')
        path, explored_states = astar_search(problem, problem.h)
        path_LC.append(len(path))
        explored_LC.append(explored_states)
        problem = FifteenPuzzle(initial_state, 'LinC')
        path, explored_states = astar_bidirectional_search(problem, problem.h)
        path_bi_LC.append(len(path))
        explored_bi_LC.append(explored_states)

    mean_LC = []
    mean_bi_LC = []
    for i in range(0, 10):
        mean_LC.append(statistics.mean(explored_LC[i*10:i*10+9]))
        mean_bi_LC.append(statistics.mean(explored_bi_LC[i*10:i*10+9]))

    X_axis = np.arange(len(x))
    plt.subplot(2, 1, 1)
    plt.bar(X_axis - 0.2, mean_LC, 0.4, label='A* algorithm using Manhattan Distance + Linear Conflicts')
    plt.bar(X_axis + 0.2, mean_bi_LC, 0.4, label='Bidirectional A* algorithm using Manhattan Distance + Linear Conflicts')

    plt.xticks(X_axis, x)
    plt.xlabel('board')
    plt.ylabel('explored states')
    plt.title("")
    plt.legend()

    mean_LC = []
    mean_bi_LC = []
    for i in range(0, 10):
        mean_LC.append(statistics.mean(path_LC[i*10:i*10+9]))
        mean_bi_LC.append(statistics.mean(path_bi_LC[i*10:i*10+9]))
    plt.subplot(2, 1, 2)
    plt.bar(X_axis - 0.2, mean_LC, 0.4, label='A* algorithm using Manhattan Distance + Linear Conflicts')
    plt.bar(X_axis + 0.2, mean_bi_LC, 0.4, label='Bidirectional A* algorithm using Manhattan Distance + Linear Conflicts')
    plt.xticks(X_axis, x)
    plt.xlabel('board')
    plt.ylabel('solution length')
    plt.title("")
    plt.legend()
    plt.show()


test()
