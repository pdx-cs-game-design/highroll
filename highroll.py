# Note: the reasoning isn't currently right here. The
# first player must beat *both* the second and third players
# to win. This calculation only accounts for the first player beating
# the second player.

# Probability of winning given a target score to beat
# and a matrix of probabilities that a subsequent player
# will win.
def p(target, pp):
    pt = 0
    for r in range(1, 7):
        # Probability of winning when stopping after first roll of r.
        p1 = int(r > target) * (1 - pp[r])

        # Probability of winning on second roll after first roll of r.
        p2 = 0
        for s in range(1, 7):
            if r + s > 6:
                continue
            p2 += int(target < r + s) * (1 - pp[r + s]) / 6

        pt += max(p1, p2) / 6

    return pt

ps = dict()
ps[4] = {i : 0 for i in range(1, 7)}
ps[3] = {target : p(target, ps[4]) for target in range(1, 7)}
ps[2] = {target : p(target, ps[3]) for target in range(1, 7)}
ps[1] = p(0, ps[2])

for player in range(1, 4):
    print(ps[player])
