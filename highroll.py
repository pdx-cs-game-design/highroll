def p(target, pp):
    t1 = 0
    for r in range(target+1, 7):
        t1 += 1 - pp[r]
    t1 /= 6

    t2 = 0
    for r in range(1, target+1):
        t2r = 0
        for s in range(1, 7):
            t2r += int(target < r + s and r + s <= 6) * (1 - pp[s])
        t2r /= 6
        t2 += t2r
    t2 /= max(target, 1)
    return t1 + (1 - t1) * t2

ps = dict()
ps[4] = {i : 0 for i in range(1, 7)}
ps[3] = {target : p(target, ps[4]) for target in range(1, 7)}
ps[2] = {target : p(target, ps[3]) for target in range(1, 7)}
ps[1] = {target : p(0, ps[2]) for target in range(1, 7)}

for player in range(1, 4):
    print(ps[player])
