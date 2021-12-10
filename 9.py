from utils import get_input
from functools import reduce

source = [[int(val) for val in row] for row in get_input(day=9).split("\n")]

# values = [
#     "2199943210",
#     "3987894921",
#     "9856789892",
#     "8767896789",
#     "9899965678",
# ]
# source = [[int(val) for val in row] for row in values]
width = len(source[0])
height = len(source)

readings = {
    (x, y): source[y][x] for y in range(len(source)) for x in range(len(source[y]))
}


def get_neighbors(coord):
    neighbors = [
        (coord[0] + x_offset, coord[1] + y_offset)
        for x_offset, y_offset in ((0, -1), (0, 1), (1, 0), (-1, 0))
    ]

    return [
        val
        for val in neighbors
        if val[0] >= 0 and val[0] < width and val[1] >= 0 and val[1] < height
    ]


low_points = []
for coord, val in readings.items():
    neighbors = get_neighbors(coord)
    if all(val < readings[neigh] for neigh in neighbors):
        low_points.append(val)

print("Part 1:")
print(sum([point + 1 for point in low_points]))

low_coords = set(
    coord
    for coord, val in readings.items()
    if all(val < readings[neigh] for neigh in neighbors)
)


def find_basin(coord, path):
    neighbors = get_neighbors(coord)
    targets = [
        neigh
        for neigh in neighbors
        if readings[coord] <= readings[neigh]
        and readings[neigh] != 9
        and neigh not in path
    ]

    for target in targets:
        path.add(target)
        find_basin(target, path)


basin_sizes = []
for low_coord in low_coords:
    result = {low_coord}
    find_basin(low_coord, result)
    # print(f"{low_coord} basin size: {len(result)}")
    basin_sizes.append(len(result))

basin_sizes = sorted(basin_sizes, reverse=True)[:10]
print(basin_sizes)
print("Part 2")
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
