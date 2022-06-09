from LinearConflicts import linearConflicts
import ManhattanDistance


class FifteenPuzzle:

    def __init__(self, initial, heuristic=None, goal=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)):
        self.initial = initial
        self.goal = goal
        self.heuristic = heuristic

    def find_blank_square(self, state):
        return state.index(0)

    def actions(self, state):

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % 4 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 4:
            possible_actions.remove('UP')
        if index_blank_square % 4 == 3:
            possible_actions.remove('RIGHT')
        if index_blank_square > 11:
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -4, 'DOWN': 4, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        return state == self.goal

    def check_solvability(self, state):

        inversion = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                    inversion += 1

        return (inversion % 2 == 0 and self.find_blank_square(state) // 4 in (1, 3)) or (
                    inversion % 2 == 1 and self.find_blank_square(state) // 4 in (0, 2))

    def h(self, node):
        # The heuristic function
        if self.heuristic == 'man':
            return ManhattanDistance.manhattanDistance(node.state, self.goal)
        if self.heuristic == 'LinC':
            return linearConflicts(node.state, self.goal)
        else:
            return sum(s != g for (s, g) in zip(node.state, self.goal))

    def path_cost(self, c):
        return c + 1


class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        # Create un nodo nell'albero di ricerca, deriveto da parent attraverso action.
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        # Crea una lista di nodi accessibili con un'unica azione da questo nodo.
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost))
        return next_node

    def path(self):
        # Ritorna la lista di nodi che costituiscono il cammino dalla radice a questo nodo.
        node = self
        path_back = []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))



