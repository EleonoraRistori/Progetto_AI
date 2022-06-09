import numpy as np
from FifteenPuzzleProblem import FifteenPuzzle, Node
from PriorityQueue import PriorityQueue


def biBF_search(problemF, f):
    problemB = FifteenPuzzle(problemF.goal, problemF.heuristic, problemF.initial)
    nodeF = Node(problemF.initial)
    nodeB = Node(problemB.initial)
    frontierF = PriorityQueue('min', f)
    frontierF.append(nodeF)
    frontierB = PriorityQueue('min', lambda n: n.path_cost + problemB.h(n))
    frontierB.append(nodeB)
    reachedF = dict()
    reachedB = dict()
    explored = 0
    reachedF[nodeF.state] = nodeF
    reachedB[nodeB.state] = nodeB
    solution = None
    while solution is None:
        if frontierF.top() < frontierB.top():
            solution = proceed(1, f, problemF, frontierF, reachedF, reachedB)
        else:
            solution = proceed(2, lambda n: n.path_cost + problemB.h(n), problemB, frontierB, reachedB, reachedF)
        explored += 1
    solution = terminated(solution, frontierF, frontierB, problemF, problemB, reachedF, reachedB, f, lambda n: n.path_cost + problemB.h(n))
    return solution, explored


def proceed(dir, f, problemF, frontierF, reachedF, reachedB):
    node = frontierF.pop()
    for child in node.expand(problemF):
        if child.state in reachedB:
            pathAdapted = adaptPath(dir, child, reachedB, problemF)
            return pathAdapted
        if child.state not in reachedF and child not in frontierF:
            reachedF[child.state] = child
            frontierF.append(child)
        elif child in frontierF:
            if f(child) < frontierF[child]:
                del frontierF[child]
                frontierF.append(child)
    return None


def adaptPath(dir, node_stop, reachedB, problemF):
    path = []
    if dir == 1:
        node = Node(node_stop.state, node_stop.parent, node_stop.action, node_stop.path_cost)
        while node:
            path.append(node)
            node = node.parent
        path = list(reversed(path))
        m = np.inf
        for child in node_stop.expand(problemF):
            if child.state in reachedB and child.path_cost < m:
                m = child.path_cost
                node = reachedB[child.state]
        while node:
            path.append(node)
            node = node.parent
        return path
    if dir == 2:
        node = Node(node_stop.state, node_stop.parent, node_stop.action, node_stop.path_cost)
        while node:
            path.append(node)
            node = node.parent
        m = np.inf
        for child in node_stop.expand(problemF):
            if child.state in reachedB and child.path_cost < m:
                m = child.path_cost
                node = reachedB[child.state]
        path_back = []
        while node:
            path_back.append(node)
            node = node.parent
        path_back = list(reversed(path_back))
        for state in path:
            path_back.append(state)
        return path_back


def terminated(solution, frontierF, frontierB, problemF, problemB, reachedF, reachedB, f, g):
    if solution is not None:
        while frontierF:
            node = frontierF.pop()
            if problemF.goal_test(node.state):
                if len(node.path()) < len(solution):
                    solution = node.path()
            for child in node.expand(problemF):
                if child.state in reachedB:
                    pathAdapted = adaptPath(1, child, reachedB, problemF)
                    if len(pathAdapted) < len(solution):
                        solution = pathAdapted
                if child.state not in reachedF and child not in frontierF and f(child) < len(solution):
                    reachedF[child.state] = child
                    frontierF.append(child)
        while frontierB:
            node = frontierB.pop()
            if problemB.goal_test(node.state):
                if len(node.path()) < len(solution):
                    solution = node.path()
            for child in node.expand(problemB):
                if child.state in reachedF:
                    pathAdapted = adaptPath(2, child, reachedF, problemB)
                    if len(pathAdapted) < len(solution):
                        solution = pathAdapted
                if child.state not in reachedB and child not in frontierB and g(child) < len(solution):
                    reachedB[child.state] = child
                    frontierB.append(child)
    return solution


def astar_bidirectional_search(problem, h=None):
    if problem.check_solvability(problem.initial):
        return biBF_search(problem, lambda n: n.path_cost + h(n))
    return None, 0
