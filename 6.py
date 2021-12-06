from utils import get_input
from collections import defaultdict

counts = {day: defaultdict(int) for day in range(257)}
seed = [int(val) for val in get_input(day=6).split(",")]
# seed = [3, 4, 3, 1, 2]
counts[0] = {value: seed.count(value) for value in seed}


def next_day(today):
    for key, number in counts[today - 1].items():
        if number - 1 == -1:
            counts[today][6] += 1
            counts[today][8] += 1
        else:
            if key - 1 == -1:
                counts[today][6] += number
                counts[today][8] += number
            else:
                counts[today][key - 1] += number


for day in range(1, 257):
    next_day(day)

print(sum(v.get(8, 0) for d, v in counts.items()) + len(seed))
