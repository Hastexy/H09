# from itertools import combinations

# li = [1, 2, 3, 4, 5, 0]
# li = sorted(list(combinations(li, 2)))


# print(li)


def round_robin(units, sets=None):
    """Generates a schedule of "fair" pairings from a list of units"""
    count = len(units)
    sets = sets or (count - 1)
    half = int(count / 2)
    for turn in range(sets):
        left = units[:half]
        right = units[count - half - 1 + 1 :][::-1]
        pairings = zip(left, right)
        if turn % 2 == 1:
            pairings = [(y, x) for (x, y) in pairings]
        units.insert(1, units.pop())
        yield pairings


teams = ["a", "b", "c", "d"]
print(list(round_robin(teams, sets=len(teams) - 1)))
