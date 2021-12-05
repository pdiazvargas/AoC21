from utils import get_input
from collections import defaultdict

source = [val for val in get_input(day=5).split("\n")]

"""
  0123456789   x,y
0 .......1..  (7,0):(7,4)
1 ..1....1..  (2,1):(2,2)
2 ..1....1..
3 .......1..
4 .112111211
5 ..........
6 ..........
7 ..........
8 ..........
9 222111....
"""

# source = [
#     "0,9 -> 5,9",
#     "8,0 -> 0,8",
#     "9,4 -> 3,4",
#     "2,2 -> 2,1",
#     "7,0 -> 7,4",
#     "6,4 -> 2,0",
#     "0,9 -> 2,9",
#     "3,4 -> 1,4",
#     "0,0 -> 8,8",
#     "5,5 -> 8,2",
# ]


class Board:
    def __init__(self):
        self.points = defaultdict(int)

    def mark_range(self, start_coord, end_coord):
        """
        start_coord: (0,9)
        end_coord:   (5,9)
        """
        if start_coord[0] == end_coord[0]:
            x = start_coord[0]
            min_y = min(start_coord[1], end_coord[1])
            max_y = max(start_coord[1], end_coord[1])

            for y in range(min_y, max_y + 1):
                self.points[(x, y)] += 1

        elif start_coord[1] == end_coord[1]:
            y = start_coord[1]
            min_x = min(start_coord[0], end_coord[0])
            max_x = max(start_coord[0], end_coord[0])

            for x in range(min_x, max_x + 1):
                self.points[(x, y)] += 1
        else:
            self.points[(start_coord[0], start_coord[1])] += 1
            x_fact = -1 if start_coord[0] > end_coord[0] else 1
            y_fact = -1 if start_coord[1] > end_coord[1] else 1
            new_x, new_y = start_coord[0], start_coord[1]
            while new_x != end_coord[0] and new_y != end_coord[1]:
                new_x = x_fact + new_x
                new_y = y_fact + new_y
                self.points[(new_x, new_y)] += 1

    def get_overlap_count(self):
        return len([v for v in self.points.values() if v >= 2])


def parse_coordinate(line):
    parts = line.split(" -> ")
    start = [int(val.strip()) for val in parts[0].split(",")]
    end = [int(val.strip()) for val in parts[1].split(",")]
    return start, end


board = Board()
for line in source:
    start, end = parse_coordinate(line)
    board.mark_range(start, end)

print(board.get_overlap_count())
