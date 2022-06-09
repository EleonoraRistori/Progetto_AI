import matplotlib.pyplot as plt
from FifteenPuzzleProblem import FifteenPuzzle
from Astar import astar_search
from BidirectionalAstar import astar_bidirectional_search
from Shuffle import shuffle
import statistics
import numpy as np


shuf = 30
for i in range(0, 10):
    problem = FifteenPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0))

    initial_state = shuffle(problem, shuf)
    #print(initial_state)
    problem = FifteenPuzzle(initial_state, 'LinC')
    path, y = astar_search(problem, problem.h)
    problem = FifteenPuzzle(initial_state, 'LinC')
    path2, z = astar_bidirectional_search(problem, problem.h)
    print(path)
    print(path2)
    print(len(path), len(path2))


