from utils import get_input
from collections import Counter

source = [row for row in get_input(day=14).split("\n")]

poly = source[0]

rules = {entry.split(" -> ")[0]: entry.split(" -> ")[1] for entry in source[2:]}


def step(template):
    new_poly = []
    for i in range(len(template) - 1):
        new_poly.append(template[i])
        pair = template[i] + template[i + 1]

        if pair in rules:
            new_poly.append(rules[pair])
    new_poly.append(template[-1])
    return "".join(new_poly)


for i in range(10):
    poly = step(poly)

counter = Counter(poly)
print("Part 1")
print(max(counter.values()) - min(counter.values()))


def insert2(pairs, seq, lim):
    # for part 2, counting occurences of pairs
    c = Counter(seq)
    while lim > 0:

        new_pairs = Counter()
        # add the new pairs - after inserting the Letter by the rules in d, two new pairs are added.
        for k, f in pairs.items():
            new_pairs[k[0] + rules[k]] += f
            new_pairs[rules[k] + k[1]] += f
            # adding the count of the current pair to the newly inserted Letter by the rules (d[k]).
            c[rules[k]] += f
        pairs = new_pairs
        lim -= 1
    return max(c.values()) - min(c.values())


poly = source[0]
pairs = Counter([poly[i : i + 2] for i in range(len(poly) - 1)])
print("Part 2")
print(insert2(pairs, poly, 40))
