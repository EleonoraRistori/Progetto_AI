from FifteenPuzzleProblem import Node
from PriorityQueue import PriorityQueue


def best_first_search(problem, f):
    node = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node.path(), len(explored)
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None


def astar_search(problem, h=None):
    if problem.check_solvability(problem.initial):
        return best_first_search(problem, lambda n: n.path_cost + h(n))
    return None, 0

