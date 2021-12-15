from utils import get_input
from collections import defaultdict

source = [row for row in get_input(day=11).split("\n")]
source = [[int(v) for v in row] for row in source]
rows = len(source)
cols = len(source[0])

mat = defaultdict(
    lambda: 11, [((x, y), source[x][y]) for x in range(rows) for y in range(cols)]
)
directions = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]]
directions = [v for v in directions if v != (0, 0)]


def move_entry(starting, flashed):
    q = [starting]

    while len(q):
        position = q.pop()
        if position not in mat or position in flashed:
            continue
        if mat[position] + 1 == 10:
            mat[position] = 0
            flashed.add(position)
            for dx, dy in directions:
                q.append((position[0] + dx, position[1] + dy))
        else:
            mat[position] += 1


def mat_list():
    result = []
    for x in range(rows):
        result.append("".join([str(mat[(x, y)]) for y in range(cols)]))

    return result


result = {"flash_count": 0}


def step():
    flashes = set()

    for position in mat:
        move_entry(position, flashes)

    result["flash_count"] += len(flashes)
    return mat_list()


for i in range(100):
    step()

print("Part 1:")
print(result["flash_count"])

count = 0

while all(v == 0 for v in mat.values()) != True:
    step()
    count += 1

print(count)
