from FifteenPuzzleProblem import Node
from PriorityQueue import PriorityQueue


def best_first_search(problem, f, display=False):
    node = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            if display:
                print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
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


def astar_search(problem, h=None, display=False):
    if problem.check_solvability(problem.initial):
        return best_first_search(problem, lambda n: n.path_cost + h(n), display)
    return None, 0

