def sense(p, motion, world, p_hit, p_miss):
    n = []
    for i in range(len(world)):
        m = []
        for j in range(len(world[i])):
            hit = (motion == world[i][j])
            m.append(p[i][j] * (hit * p_hit + (1 - hit) * p_miss))
        n.append(m)
    return normalize(n)


def normalize(n):
    s = 0
    for i in range(len(n)):
        s += sum(n[i])

    for i in range(len(n)):
        for j in range(len(n[i])):
            n[i][j] = (n[i][j] / s)
    return n
