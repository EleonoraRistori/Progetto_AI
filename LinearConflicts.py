import numpy
import ManhattanDistance


def conflict_rows(cj, ri, state, goal):
    c = 0
    conflict_tiles = []
    if goal.index(state[ri * 4 + cj]) // 4 == ri:
        for i in range(0, 4):
            if state[ri * 4 + i] != 0:
                if ri*4+i < ri*4+cj and goal.index(state[ri * 4 + i]) // 4 == ri and goal.index(state[ri * 4 + i]) > goal.index(state[ri * 4 + cj]):
                    c = c+1
                    conflict_tiles.append(ri*4+i)
                if ri*4+i > ri*4+cj and goal.index(state[ri * 4 + i]) // 4 == ri and goal.index(state[ri * 4 + i]) < goal.index(state[ri * 4 + cj]):
                    c = c+1
                    conflict_tiles.append(ri*4+i)
    return c, conflict_tiles


def check_condition_rows(C, ri):
    for cj in range(0, 4):
        if C[ri*4+cj] > 0:
            return True
    return False


def LC_rows(state, goal):
    lc = numpy.zeros(4)
    C = numpy.zeros(16)
    LC = 0
    conflict_tiles = {}
    for ri in range(0, 4):
        lc[ri] = 0
        for cj in range(0, 4):
            if state[ri * 4 + cj] != 0:
                C[ri*4+cj], conflict_tiles[ri*4+cj] = conflict_rows(cj, ri, state, goal)
        while check_condition_rows(C, ri):
            ck = 0
            for cj in range(1, 4):
                if C[ri*4+cj] > C[ri*4+ck]:
                    ck = cj
            C[ri*4+ck] = 0
            for j in conflict_tiles[ri*4+ck]:
                C[j] = C[j]-1
            lc[ri] = lc[ri]+1
    for ri in range(0, 4):
        LC = LC + 2*lc[ri]
    return LC


def conflict_columns(cj, ri, state, goal):
    c = 0
    conflict_tiles = []
    if goal.index(state[ri * 4 + cj]) % 4 == cj:
        for i in range(0, 4):
            if state[i*4+cj] != 0:
                if i*4+cj < ri*4+cj and goal.index(state[i * 4 + cj]) % 4 == cj and goal.index(state[i * 4 + cj]) > goal.index(state[ri * 4 + cj]):
                    c = c+1
                    conflict_tiles.append(i*4+cj)
                if i*4+cj > ri*4+cj and goal.index(state[i * 4 + cj]) % 4 == cj and goal.index(state[i * 4 + cj]) < goal.index(state[ri * 4 + cj]):
                    c = c+1
                    conflict_tiles.append(i*4+cj)
    return c, conflict_tiles


def check_condition_columns(C, cj):
    for ri in range(0, 4):
        if C[ri*4+cj] > 0:
            return True
    return False


def LC_columns(state, goal):
    lc = numpy.zeros(4)
    C = numpy.zeros(16)
    LC = 0
    conflict_tiles = {}
    for cj in range(0, 4):
        lc[cj] = 0
        for ri in range(0, 4):
            if state[ri * 4 + cj] != 0:
                C[ri*4+cj], conflict_tiles[ri*4+cj] = conflict_columns(cj, ri, state, goal)
        while check_condition_columns(C, cj):
            rk = 0
            for ri in range(1, 4):
                if C[ri*4+cj] > C[rk*4+cj]:
                    rk = ri
            C[rk*4+cj] = 0
            for i in conflict_tiles[rk*4+cj]:
                C[i] = C[i]-1
            lc[cj] = lc[cj]+1
    for cj in range(0, 4):
        LC = LC + 2*lc[cj]
    return LC


def linearConflicts(state, goal):
    return LC_rows(state, goal) + LC_columns(state, goal) + ManhattanDistance.manhattanDistance(state, goal)
