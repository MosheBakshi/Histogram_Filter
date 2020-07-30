

def move(p, motions, p_exact):
    m = []
    for i in range(len(p)):
        n = []
        for j in range(len(p[i])):
            s = (p_exact * p[(i - motions[0]) % len(p)][(j - motions[1]) % len(p[i])])
            n.append(s)
        m.append(n)
    return m