from sense import *
from move import *


def histogram_localization(map_grid, measurements, motions, sensor_right, p_move, p_move_overshoot, p_move_undershoot):
    a_priory = 1.0 / (len(map_grid) * len(map_grid[0]))
    p_matrix = [ [ a_priory for row in range(len(map_grid))] for cols in range(len(map_grid[0]))]
    for i in range(len(map_grid)):
        w = [len(map_grid[i])]
        p_matrix.append(w)
    for i in range(len(motions)):
        p_matrix = move(p_matrix, motions[i], p_move)
        p_matrix = sense(p_matrix, measurements[i], map_grid, sensor_right, (1 - sensor_right))
    return p_matrix


def show(ans):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x), r)) + ']' for r in ans]
    print('[' + ',\n '.join(rows) + ']')
