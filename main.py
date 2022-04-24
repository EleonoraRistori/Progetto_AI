import random
import matplotlib.pyplot as plt
from FifteenPuzzleProblem import FifteenPuzzle
from Astar import astar_search
from BidirectionalAstar import astar_bidirectional_search
from Shuffle import shuffle


def test():
    x = []
    path_man = []
    path_LC = []
    path_bi_LC = []
    path_bi_man = []
    explored_man = []
    explored_LC = []
    explored_bi_man = []
    explored_bi_LC = []
    for i in range(0, 200):
        problem = FifteenPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))
        x.append(random.randrange(10, 50))
        initial_state = shuffle(problem, x[i])
        problem = FifteenPuzzle(initial_state, 'man')
        path, explored_states = astar_search(problem, problem.h, False)
        path_man.append(len(path))
        explored_man.append(explored_states)
        problem = FifteenPuzzle(initial_state, 'man')
        path, explored_states = astar_bidirectional_search(problem, problem.h)
        path_bi_man.append(len(path))
        explored_bi_man.append(explored_states)
        problem = FifteenPuzzle(initial_state, 'LinC')
        path, explored_states = astar_search(problem, problem.h)
        path_LC.append(len(path))
        explored_LC.append(explored_states)
        problem = FifteenPuzzle(initial_state, 'LinC')
        path, explored_states = astar_bidirectional_search(problem, problem.h)
        path_bi_LC.append(len(path))
        explored_bi_LC.append(explored_states)

    plt.rcParams.update({'font.size': 14})
    plt.subplot(2, 1, 1)
    plt.scatter(x, path_man)
    plt.scatter(x, path_LC)
    plt.scatter(x, path_bi_man)
    plt.scatter(x, path_bi_LC)
    plt.xlabel('board')
    plt.ylabel('solution length')
    plt.legend(['A* algorithm using Manhattan Distance', 'A* algorithm using Linear Conflicts',
                'Bidirectional A* using Manhattan Distance', 'Bidirectional A* using Linear Conflicts'])
    plt.subplot(2, 1, 2)
    plt.scatter(x, explored_man)
    plt.scatter(x, explored_LC)
    plt.scatter(x, explored_bi_man)
    plt.scatter(x, explored_bi_LC)
    plt.xlabel('board')
    plt.ylabel('explored states')

    plt.show()


test()

