from utils import get_input
from collections import defaultdict

source = [row for row in get_input(day=13).split("\n")]
paper = defaultdict(bool)

# source = [
#     "6,10",
#     "0,14",
#     "9,10",
#     "0,3",
#     "10,4",
#     "4,11",
#     "6,0",
#     "6,12",
#     "4,1",
#     "0,13",
#     "10,12",
#     "3,4",
#     "3,0",
#     "8,4",
#     "1,10",
#     "2,14",
#     "8,10",
#     "9,0",
# ]


for line in source:
    if line == "":
        break
    x, y = line.split(",")
    paper[(int(x), int(y))] = True

folds = [line.replace("fold along ", "") for line in source if "fold" in line]
folds = [(line.split("=")[0], int(line.split("=")[1])) for line in folds]
print(folds)


def horizontal_fold(sheet, row):
    # Fold along the y axis
    # keep the points above the target row
    new_sheet = {}
    for coord, value in sheet.items():
        x, y = coord
        if y < row:
            new_sheet[(x, y)] = value
        else:
            dy = y - row
            new_sheet[(x, row - dy)] = True
    return new_sheet


def vertical_fold(sheet, col):
    # Fold along the x axis
    # keep the points above the target row
    new_sheet = {}
    for coord, value in sheet.items():
        x, y = coord
        if x < col:
            new_sheet[(x, y)] = value
        else:
            dx = x - col
            new_sheet[(col - dx, y)] = True
    return new_sheet


for fold in folds:
    if fold[0] == "x":
        paper = vertical_fold(paper, fold[1])
    else:
        paper = horizontal_fold(paper, fold[1])


board = []
for row in range(40):
    board.append(
        "".join(["X" if paper.get((row, col), False) else "." for col in range(40)])
    )

print("\n".join(board))

# new_paper = horizontal_fold(paper, 7)
# coords = [
#     (0, 0),
#     (0, 1),
#     (0, 3),
#     (1, 4),
#     (2, 0),
#     (3, 0),
#     (3, 4),
#     (4, 1),
#     (4, 3),
#     (6, 0),
#     (6, 2),
#     (6, 4),
#     (8, 4),
#     (9, 0),
#     (9, 4),
#     (10, 2),
#     (10, 4),
# ]
# assert all(new_paper[coord] for coord in coords)
# print(len(new_paper))

# coords = [
#     (0, 0),
#     (0, 1),
#     (0, 2),
#     (0, 3),
#     (0, 4),
#     (1, 0),
#     (1, 4),
#     (2, 0),
#     (2, 4),
#     (3, 0),
#     (3, 4),
#     (4, 0),
#     (4, 1),
#     (4, 2),
#     (4, 3),
#     (4, 4),
# ]
# new_paper = vertical_fold(new_paper, 5)
# assert all(new_paper[coord] for coord in coords)

# print(len(new_paper))
