import matplotlib.pyplot as plt
from FifteenPuzzleProblem import FifteenPuzzle
from Astar import astar_search
from BidirectionalAstar import astar_bidirectional_search
from Shuffle import shuffle
import statistics
import numpy as np

""" Funzione che confronta gli algoritmi A* e A* bidirezionale utilizzando le euristiche Manhattan e Linear Conflicts.
    Il grafico mostra il numero di stati esplorati nei quattro casi. Il codice commentato consente
    di ottenere un ulteriore grafico che mostra la lunghezza delle soluzioni nei 4 casi a conferma
    dell'ottimalità dei due algoritmi"""


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
    shuf = 5
    for i in range(0, 100):
        problem = FifteenPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))
        if i % 10 == 0:
            shuf += 5
            x.append(shuf)
        initial_state = shuffle(problem, shuf)
        problem = FifteenPuzzle(initial_state, 'man')
        path, explored_states = astar_search(problem, problem.h)
        path_man.append(len(path))
        print(path)
        explored_man.append(explored_states)
        problem = FifteenPuzzle(initial_state, 'man')
        path, explored_states = astar_bidirectional_search(problem, problem.h)
        print(path)
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

    mean_man = []
    mean_LC = []
    mean_bi_man = []
    mean_bi_LC = []
    for i in range(0, 10):
        mean_man.append(statistics.mean(explored_man[i*10:i*10+9]))
        mean_LC.append(statistics.mean(explored_LC[i*10:i*10+9]))
        mean_bi_man.append(statistics.mean(explored_bi_man[i*10:i*10+9]))
        mean_bi_LC.append(statistics.mean(explored_bi_LC[i*10:i*10+9]))

    X_axis = np.arange(len(x))
    #plt.subplot(2, 1, 1)
    plt.bar(X_axis - 0.3, mean_man, 0.2, label='A* algorithm using Manhattan Distance')
    plt.bar(X_axis - 0.1, mean_LC, 0.2, label='A* algorithm using Manhattan Distance + Linear Conflicts')
    plt.bar(X_axis + 0.1, mean_bi_man, 0.2, label='Bidirectional A* algorithm using Manhattan Distance')
    plt.bar(X_axis + 0.3, mean_bi_LC, 0.2, label='Bidirectional A* algorithm using Manhattan Distance + Linear Conflicts')

    plt.xticks(X_axis, x)
    plt.xlabel('board')
    plt.ylabel('explored states')
    plt.title("")
    plt.legend()

    """mean_man = []
    mean_LC = []
    mean_bi_man = []
    mean_bi_LC = []
    for i in range(0, 10):
        mean_man.append(statistics.mean(path_man[i*10:i*10+9]))
        mean_LC.append(statistics.mean(path_LC[i*10:i*10+9]))
        mean_bi_man.append(statistics.mean(path_bi_man[i*10:i*10+9]))
        mean_bi_LC.append(statistics.mean(path_bi_LC[i*10:i*10+9]))
    plt.subplot(2, 1, 2)
    plt.bar(X_axis - 0.3, mean_man, 0.2, label='A* algorithm using Manhattan Distance')
    plt.bar(X_axis - 0.1, mean_LC, 0.2, label='A* algorithm using Manhattan Distance + Linear Conflicts')
    plt.bar(X_axis + 0.1, mean_bi_man, 0.2, label='Bidirectional A* algorithm using Manhattan Distance')
    plt.bar(X_axis + 0.3, mean_bi_LC, 0.2, label='Bidirectional A* algorithm using Manhattan Distance + Linear Conflicts')
    plt.xticks(X_axis, x)
    plt.xlabel('board')
    plt.ylabel('solution length')
    plt.title("")
    plt.legend()"""
    plt.show()


test()
