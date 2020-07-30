##
# Main function of the Python program.
#
##

from histogram import *


def main():
    Map = [['G', 'G', 'G'],
           ['G', 'R', 'R'],
           ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0, 1], [1, 0]]
    sensor_right = 0.9
    p_move = 1
    p_move_overshoot = 0.1
    p_move_undershoot = 0.1
    ans = []
    for i in range(len(Map)):
        w = [len(Map[i])]
        ans.append(w)
    ans = histogram_localization(Map, measurements, motions, sensor_right, p_move, p_move_overshoot, p_move_undershoot)
    show(ans)  # displays your answer
    print(ans[0])


if __name__ == '__main__':
    main()
