import matplotlib.pyplot as plt
from FifteenPuzzleProblem import FifteenPuzzle
from BidirectionalAstar import astar_bidirectional_search
from Shuffle import shuffle
import statistics
import numpy as np

""" Funzione che confronta le euristiche Manhattan e Linear Conflicts ed il numero di celle errate 
    applicate all'algoritmo A*. Il grafico mostra il numero di stati esplorati nei 3 casi."""

def test():
    x = []
    path_wrong = []
    path_man = []
    path_LC = []
    explored_wrong = []
    explored_man = []
    explored_LC = []
    shuf = 20
    for i in range(0, 100):
        problem = FifteenPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))
        if i % 10 == 0 and i != 0:
            shuf += 1
        x.append(shuf)
        initial_state = shuffle(problem, x[i])
        problem = FifteenPuzzle(initial_state)
        path, explored_states = astar_bidirectional_search(problem, problem.h)
        path_wrong.append(len(path))
        explored_wrong.append(explored_states)
        problem = FifteenPuzzle(initial_state, 'man')
        path, explored_states = astar_bidirectional_search(problem, problem.h)
        path_man.append(len(path))
        explored_man.append(explored_states)
        problem = FifteenPuzzle(initial_state, 'LinC')
        path, explored_states = astar_bidirectional_search(problem, problem.h)
        path_LC.append(len(path))
        explored_LC.append(explored_states)

    X = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    mean_wrong = []
    mean_man = []
    mean_LC = []
    for i in range(0, 10):
        mean_wrong.append(statistics.mean(explored_wrong[i*10:i*10+9]))
        mean_man.append(statistics.mean(explored_man[i*10:i*10+9]))
        mean_LC.append(statistics.mean(explored_LC[i*10:i*10+9]))

    X_axis = np.arange(len(X))

    plt.bar(X_axis - 0.3, mean_wrong, 0.3, label='Bidirectional A* algorithm using number of wrong tiles heuristic')
    plt.bar(X_axis, mean_man, 0.3, label='Bidirectional A* algorithm using Manhattan Distance')
    plt.bar(X_axis + 0.3, mean_LC, 0.3, label='Bidirectional A* algorithm using Manhattan Distance + Linear Conflicts')

    plt.xticks(X_axis, X)
    plt.xlabel('board')
    plt.ylabel('explored states')
    plt.title("")
    plt.legend()
    plt.show()


test()
